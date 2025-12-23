import asyncio
import string
import time
from contextlib import asynccontextmanager
from pathlib import Path

import httpx
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from src.config import get_settings
from src.logging_config import get_logger, setup_logging
from src.robot_service import RobotService

setup_logging()
logger = get_logger(__name__)

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
        if time.monotonic() < expiry:
            return value
        del _cache[key]
    return None


def cache_set(key: str, value: str, timeout: int) -> None:
    expiry = time.monotonic() + timeout
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
    # Startup: initialize services and create background tasks
    await robot_service.start()
    numeric_task = asyncio.create_task(poll_numeric_registers())
    string_task = asyncio.create_task(poll_string_registers())
    logger.info("background_polling_started")

    yield

    # Shutdown: cancel background tasks and cleanup
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
    await robot_service.stop()
    logger.info("background_polling_stopped")


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

    registers_html = templates.get_template("registers.html").render(
        {"request": request, "numeric_registers": numeric_registers}
    )

    timer_html = templates.get_template("timer.html").render(
        {"request": request, "timer_value": timer_value}
    )

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
            logger.error("quote_fetch_failed", error=str(e))
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
        logger.info("keypress", key=data["key"])

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
        logger.warning("invalid_keypress")
        return JSONResponse({"error": "Invalid key pressed"}, status_code=400)


def run():
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=5000, log_config=None)


if __name__ == "__main__":
    run()
