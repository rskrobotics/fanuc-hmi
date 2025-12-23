import asyncio
import logging
import string
from contextlib import asynccontextmanager
from logging.handlers import RotatingFileHandler
from pathlib import Path

import httpx
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from src.config import get_settings
from src.robot_service import RobotService

# Logging setup
logging.basicConfig(level=logging.INFO)

handler = RotatingFileHandler("hmi.log", maxBytes=10000, backupCount=3)
formatter = logging.Formatter(
    "%(asctime)s %(levelname)s: %(message)s [in %(module)s:%(lineno)d]"
)
handler.setFormatter(formatter)
handler.setLevel(logging.DEBUG)
root_logger = logging.getLogger()
root_logger.addHandler(handler)
root_logger.setLevel(logging.DEBUG)

# Silence noisy loggers
logging.getLogger("httpcore").setLevel(logging.WARNING)
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

# Settings and services
settings = get_settings()
robot_service = RobotService(
    ip_address=settings.robot.ip,
    mock_data=settings.mock_robot,
)

# Simple in-memory cache
_cache: dict[str, tuple[str, float]] = {}


def cache_get(key: str) -> str | None:
    if key in _cache:
        value, expiry = _cache[key]
        if asyncio.get_event_loop().time() < expiry:
            return value
        del _cache[key]
    return None


def cache_set(key: str, value: str, timeout: int) -> None:
    expiry = asyncio.get_event_loop().time() + timeout
    _cache[key] = (value, expiry)


# Background tasks
async def poll_numeric_registers():
    interval = settings.fetch_intervals.seconds_numeric
    while True:
        await robot_service.fetch_numeric_registers()
        await asyncio.sleep(interval)


async def poll_string_registers():
    interval = settings.fetch_intervals.seconds_string
    # Initial delay before first fetch
    await asyncio.sleep(8)
    while True:
        await robot_service.fetch_string_registers()
        await asyncio.sleep(interval)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: create background tasks
    numeric_task = asyncio.create_task(poll_numeric_registers())
    string_task = asyncio.create_task(poll_string_registers())
    logger.info("Background polling tasks started")

    yield

    # Shutdown: cancel background tasks
    numeric_task.cancel()
    string_task.cancel()
    try:
        await numeric_task
    except asyncio.CancelledError:
        pass
    try:
        await string_task
    except asyncio.CancelledError:
        pass
    logger.info("Background polling tasks stopped")


app = FastAPI(lifespan=lifespan)

# Static files and templates
app_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=app_dir / "static"), name="static")
templates = Jinja2Templates(directory=app_dir / "templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/update-data", response_class=HTMLResponse)
async def update_data(request: Request):
    all_numeric_registers = robot_service.get_numeric_registers()
    displayed_numeric_indices = settings.displayed_registers.numeric

    # Extract the value for register 28 (timer)
    timer = next((reg for reg in all_numeric_registers if reg.id == 28), None)
    timer_value = timer.value if timer else None

    numeric_registers = [
        reg for reg in all_numeric_registers if reg.id in displayed_numeric_indices
    ]

    registers_html = templates.TemplateResponse(
        "registers.html",
        {"request": request, "numeric_registers": numeric_registers},
    ).body.decode()

    timer_html = templates.TemplateResponse(
        "timer.html",
        {"request": request, "timer_value": timer_value},
    ).body.decode()

    return HTMLResponse(content=registers_html + timer_html)


@app.get("/update-message", response_class=HTMLResponse)
async def update_message(request: Request):
    message = cache_get("cached_message")
    template_color_class = "default-color"

    if message is None:
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(settings.quote_api_url, timeout=5.0)
                if response.status_code == 200:
                    quote_data = response.json()
                    message = quote_data.get("quoteText")
                    if quote_data.get("quoteAuthor"):
                        message += f" - {quote_data.get('quoteAuthor')}"
                    cache_set("cached_message", message, settings.cache_timeout_seconds)
                else:
                    message = "Default Message"
                    cache_set("cached_message", message, settings.cache_timeout_seconds)
        except (httpx.RequestError, ValueError) as e:
            # ValueError catches JSON decode errors (malformed API responses)
            logger.error(f"Quote fetch failed: {e}")
            message = "Default Message"
            cache_set("cached_message", message, settings.cache_timeout_seconds)

    string_register_index = int(
        next(
            (reg.value for reg in robot_service.numeric_registers if reg.id == 31),
            0,
        )
    )

    if string_register_index > 0:
        try:
            message_register = next(
                (
                    reg
                    for reg in robot_service.string_registers
                    if reg.id == string_register_index
                ),
                None,
            )

            if message_register is not None:
                message = message_register.value
                template_color_class = "register-color"
            else:
                raise ValueError(
                    f"No string register with identifier {string_register_index}"
                )

        except ValueError as e:
            template_color_class = "error-color"
            message = str(e)
    elif string_register_index < 0:
        template_color_class = "error-color"
        message = "Invalid register index: Index should be positive."

    return templates.TemplateResponse(
        "message.html",
        {
            "request": request,
            "message": message,
            "template_color_class": template_color_class,
        },
    )


@app.post("/keypress")
async def keypress(request: Request):
    data = await request.json()

    if data and data.get("key", "").lower() in string.ascii_lowercase:
        logger.info(f"{data['key']} key was pressed")

        await robot_service.set_numeric_register_value(
            register_index=settings.trigger.register_id,
            value=settings.trigger.value,
        )

        async def reset_value():
            await asyncio.sleep(settings.trigger.revert_delay_seconds)
            await robot_service.set_numeric_register_value(
                register_index=settings.trigger.register_id,
                value=settings.trigger.revert_value,
            )

        # Fire and forget the reset task
        asyncio.create_task(reset_value())

        return JSONResponse({"status": "success"}, status_code=200)

    else:
        logger.warning("Invalid key was pressed")
        return JSONResponse({"error": "Invalid key pressed"}, status_code=400)


def run():
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=5000)


if __name__ == "__main__":
    run()
