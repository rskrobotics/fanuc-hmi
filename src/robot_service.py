import asyncio
import logging
import random

import httpx

from src.domain.numeric_register import NumericRegister
from src.domain.string_register import StringRegister
from src.numeric_register_parser import parse_html_content_onto_numeric_registers
from src.string_register_parser import parse_html_content_onto_string_registers

logger = logging.getLogger(__name__)


class RobotService:
    def __init__(self, ip_address: str, mock_data: bool):
        self._lock = asyncio.Lock()
        self.ip_address = ip_address
        self.mock_data = mock_data
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

    async def fetch_numeric_registers(self):
        numeric_url = f"http://{self.ip_address}/karel/ComGet?sFc=28"

        if self.mock_data:
            async with self._lock:
                for i in range(200):
                    self.numeric_registers[i].value = round(random.uniform(0, 100), 2)
            return

        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(numeric_url, timeout=5.0)
                if response.status_code == 200:
                    async with self._lock:
                        new_values = self.parse_numeric_registers(response.text)
                        for i, element in enumerate(new_values):
                            self.numeric_registers[i].value = element.value
                            self.numeric_registers[i].comment = element.comment
                else:
                    logger.error(
                        f"Error fetching numeric registers: {response.status_code}"
                    )
        except httpx.RequestError as e:
            logger.error(f"Request failed: {e}")

    async def fetch_string_registers(self):
        logger.info("Fetching string registers...")

        if self.mock_data:
            return

        string_url = f"http://{self.ip_address}/karel/ComGet?sFc=30"

        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(string_url, timeout=5.0)
                if response.status_code == 200:
                    async with self._lock:
                        new_values = self.parse_string_registers(response.text)
                        for i, value in enumerate(new_values):
                            self.string_registers[i] = value
                else:
                    logger.error(
                        f"Error fetching string registers: {response.status_code}"
                    )
        except httpx.RequestError as e:
            logger.error(f"Request failed: {e}")

    async def set_numeric_register_value(self, register_index: int, value: int):
        if self.mock_data:
            logger.info("Mock data mode is on. Triggering in mock...")
            return

        set_url = f"http://{self.ip_address}/karel/ComSet"
        params = {
            "sFc": "2",
            "sIndx": str(register_index),
            "sValue": str(value),
            "sRealFlag": "-1",
        }

        logger.info(f"Sending request to {set_url} with params {params}")

        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(set_url, params=params, timeout=2.0)

                logger.info(f"Response status code: {response.status_code}")
                if response.status_code == 200:
                    logger.info("Successfully set register value")
                else:
                    logger.error(
                        f"Failed to set register value. Response status code: {response.status_code}"
                    )
                    logger.error(f"Response text: {response.text}")
        except httpx.RequestError as e:
            logger.error(f"Setting register value failed: {e}")
        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")

    @staticmethod
    def parse_numeric_registers(response_text: str):
        return parse_html_content_onto_numeric_registers(response_text)

    @staticmethod
    def parse_string_registers(response_text: str):
        return parse_html_content_onto_string_registers(response_text)

    def get_numeric_registers(self) -> list[NumericRegister]:
        # Synchronous read - safe because we only mutate under async lock
        return self.numeric_registers
