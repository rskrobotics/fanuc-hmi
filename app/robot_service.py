import logging
import random
from threading import Lock

import requests

from domain.numeric_register import NumericRegister
from domain.string_register import StringRegister
from numeric_register_parser import parse_html_content_onto_numeric_registers
from string_register_parser import parse_html_content_onto_string_registers

logger = logging.getLogger(__name__)


class RobotService:
    def __init__(self, ip_address, mock_data):
        self.lock = Lock()
        self.ip_address = ip_address
        self.mock_data = mock_data
        self.numeric_registers = [NumericRegister(
            id=i + 1, value=0, comment=f'Comment {i + 1}') for i in range(200)]
        self.string_registers = [StringRegister(
            id=i + 1, value=f"Message {i + 1}", comment=f"Comment {i + 1}") for i in range(25)]

    def fetch_numeric_registers(self):
        numeric_url = f'http://{self.ip_address}/karel/ComGet?sFc=28'
        if self.mock_data:
            with self.lock:
                for i in range(200):
                    self.numeric_registers[i].value = random.randint(0, 100)
            return
        try:
            response = requests.get(numeric_url)
            if response.status_code == 200:
                with self.lock:
                    new_values = self.parse_numeric_registers(response.text)
                    for i, element in enumerate(new_values):
                        self.numeric_registers[i].value = element.value
                        self.numeric_registers[i].comment = element.comment
            else:
                logger.error(f"Error fetching numeric registers: {response.status_code}")
        except requests.exceptions.RequestException as e:
            logger.error(f"Request failed: {e}")

    def fetch_string_registers(self):
        logger.info("Fetching string registers...")
        print(f"Fetching string registers")
        if self.mock_data:
            return
        string_url = f'http://{self.ip_address}/karel/ComGet?sFc=30'
        try:
            response = requests.get(string_url)
            if response.status_code == 200:
                with self.lock:
                    new_values = self.parse_string_registers(response.text)
                    for i, value in enumerate(new_values):
                        self.string_registers[i] = value
            else:
                logger.error(f"Error fetching string registers: {response.status_code}")
        except requests.exceptions.RequestException as e:
            logger.error(f"Request failed: {e}")

    def set_numeric_register_value(self, register_index, value):
        if self.mock_data:
            logger.info("Triggering in mock...")
            return
        set_url = f'http://{self.ip_address}/karel/ComGet'
        data = {
            'sFc': '3',
            'sRegIdx': register_index,
            'sValue': value
        }
        try:
            response = requests.post(set_url, data=data, timeout=2)

            if response.status_code == 200:
                logger.info("Successfully sent trigger request")
            else:
                logger.error(f"Failed to set register value. Status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            logger.error(f"Setting register value failed: {e}")

    @staticmethod
    def parse_numeric_registers(response_text):
        return parse_html_content_onto_numeric_registers(response_text)

    @staticmethod
    def parse_string_registers(response_text):
        return parse_html_content_onto_string_registers(response_text)

    def get_numeric_registers(self):
        with self.lock:
            return self.numeric_registers
