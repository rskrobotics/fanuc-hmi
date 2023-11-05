from dataclasses import asdict
import requests
from threading import Lock
from domain.numeric_register import NumericRegister
from domain.string_register import StringRegister


class RobotService:
    def __init__(self, ip_address):
        self.lock = Lock()
        self.ip_address = ip_address
        self.numeric_registers = [NumericRegister(
            id=i+1, value=0, comment=f'Comment {i+1}') for i in range(200)]
        self.string_registers = [StringRegister(
            id=i+1, value=f"Message {i+1}", comment=f"Comment {i+1}") for i in range(25)]

    def fetch_numeric_registers(self):
        numeric_url = f'http://{self.ip_address}/karel/ComGet?sFc=28'
        try:
            response = requests.get(numeric_url)
            if response.status_code == 200:
                with self.lock:
                    new_values = self.parse_numeric_registers(response.text)
                    for i, value in enumerate(new_values):
                        self.numeric_registers[i].value = value
            else:
                print(
                    f"Error fetching numeric registers: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")

    def fetch_string_registers(self):
        string_url = f'http://{self.ip_address}/karel/ComGet?sFc=30'
        try:
            response = requests.get(string_url)
            if response.status_code == 200:
                with self.lock:
                    new_values = self.parse_string_registers(response.text)
                    for i, value in enumerate(new_values):
                        self.string_registers[i].value = value
            else:
                print(
                    f"Error fetching string registers: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")

    def get_robot_data(self):
        with self.lock:
            return {
                'numeric_registers': [asdict(reg) for reg in self.numeric_registers],
                'string_registers': [asdict(reg) for reg in self.string_registers],
            }

    def set_numeric_register_value(self, register_index, value):
        print(f"Triggering...")
        set_url = f'http://{self.ip_address}/karel/ComGet'
        data = {
            'sFc': '3',
            'sRegIdx': register_index,
            'sValue': value
        }
        try:
            response = requests.post(set_url, data=data, timeout=2)
            
            if response.status_code == 200:
                print(f"Successfully sent trigger request")
            else:
                print(
                    f"Failed to set register value. Status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Setting register value failed: {e}")

    def parse_numeric_registers(self, response_text):
        pass

    def parse_string_registers(self, response_text):
        pass
