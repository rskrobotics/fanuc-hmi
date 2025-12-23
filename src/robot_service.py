import asyncio
import random

import httpx

from src.domain.numeric_register import NumericRegister
from src.domain.string_register import StringRegister
from src.logging_config import get_logger
from src.numeric_register_parser import parse_html_content_onto_numeric_registers
from src.string_register_parser import parse_html_content_onto_string_registers

logger = get_logger(__name__)


class RobotService:
    def __init__(self, ip_address: str, mock_data: bool):
        self._lock = asyncio.Lock()
        self.ip_address = ip_address
        self.mock_data = mock_data
        self._client: httpx.AsyncClient | None = None
        self.numeric_registers = [
            NumericRegister(id=i + 1, value=0, comment=f"Comment {i + 1}")
            for i in range(200)
        ]
        self.string_registers = [
            StringRegister(
                id=i + 1, value=f"Message {i + 1}", comment=f"Comment {i + 1}"
            )
            for i in range(25)
        ]

    async def start(self) -> None:
        """Initialize the HTTP client. Call this on app startup."""
        self._client = httpx.AsyncClient(timeout=5.0)

    async def stop(self) -> None:
        """Close the HTTP client. Call this on app shutdown."""
        if self._client:
            await self._client.aclose()
            self._client = None

    @property
    def client(self) -> httpx.AsyncClient:
        if self._client is None:
            raise RuntimeError("RobotService not started. Call start() first.")
        return self._client

    async def fetch_numeric_registers(self):
        numeric_url = f"http://{self.ip_address}/karel/ComGet?sFc=28"

        if self.mock_data:
            async with self._lock:
                for i in range(200):
                    # R[31] controls message display: 0 = show quotes, >0 = show string register
                    if i == 30:  # index 30 = R[31]
                        self.numeric_registers[i].value = 0
                    else:
                        self.numeric_registers[i].value = round(
                            random.uniform(0, 100), 2
                        )
            return

        try:
            response = await self.client.get(numeric_url)
            if response.status_code == 200:
                async with self._lock:
                    new_values = self.parse_numeric_registers(response.text)
                    for i, element in enumerate(new_values):
                        self.numeric_registers[i].value = element.value
                        self.numeric_registers[i].comment = element.comment
            else:
                logger.error(
                    "fetch_numeric_registers_failed", status_code=response.status_code
                )
        except httpx.RequestError as e:
            logger.error("fetch_numeric_registers_failed", error=str(e))

    async def fetch_string_registers(self):
        logger.info("fetch_string_registers")

        if self.mock_data:
            return

        string_url = f"http://{self.ip_address}/karel/ComGet?sFc=30"

        try:
            response = await self.client.get(string_url)
            if response.status_code == 200:
                async with self._lock:
                    new_values = self.parse_string_registers(response.text)
                    for i, value in enumerate(new_values):
                        self.string_registers[i] = value
            else:
                logger.error(
                    "fetch_string_registers_failed", status_code=response.status_code
                )
        except httpx.RequestError as e:
            logger.error("fetch_string_registers_failed", error=str(e))

    async def set_numeric_register_value(self, register_index: int, value: int):
        if self.mock_data:
            logger.info("set_register_mock", register=register_index, value=value)
            return

        set_url = f"http://{self.ip_address}/karel/ComSet"
        params = {
            "sFc": "2",
            "sIndx": str(register_index),
            "sValue": str(value),
            "sRealFlag": "-1",
        }

        logger.info(
            "set_register_request", url=set_url, register=register_index, value=value
        )

        try:
            response = await self.client.get(set_url, params=params, timeout=2.0)

            if response.status_code == 200:
                logger.info("set_register_success", register=register_index)
            else:
                logger.error(
                    "set_register_failed",
                    register=register_index,
                    status_code=response.status_code,
                    response=response.text,
                )
        except httpx.RequestError as e:
            logger.error("set_register_failed", register=register_index, error=str(e))

    @staticmethod
    def parse_numeric_registers(response_text: str):
        return parse_html_content_onto_numeric_registers(response_text)

    @staticmethod
    def parse_string_registers(response_text: str):
        return parse_html_content_onto_string_registers(response_text)

    def get_numeric_registers(self) -> list[NumericRegister]:
        # Synchronous read - safe because we only mutate under async lock
        return self.numeric_registers
