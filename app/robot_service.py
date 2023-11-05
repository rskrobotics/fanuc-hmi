from dataclasses import asdict
import requests
from threading import Lock
from domain.numeric_register import NumericRegister
from domain.string_register import StringRegister
from numeric_register_parser import parse_html_content_onto_numeric_registers
from string_register_parser import parse_html_content_onto_string_registers
import copy


class RobotService:
    def __init__(self, ip_address):
        self.lock = Lock()
        self.ip_address = ip_address
        self.numeric_registers = [NumericRegister(
            id=i+1, value=0, comment=f'Comment {i+1}') for i in range(200)]
        self.string_registers = [StringRegister(
            id=i+1, value=f"Message {i+1}", comment=f"Comment {i+1}") for i in range(25)]

    def fetch_numeric_registers(self):
        print("Fetching numeric registers...")
        numeric_url = f'http://{self.ip_address}/karel/ComGet?sFc=28'
        try:
            response = requests.get(numeric_url)
            print("Got a response...")
            if response.status_code == 200:
                with self.lock:
                    new_values = self.parse_numeric_registers(response.text)
                    for i, element in enumerate(new_values):
                        self.numeric_registers[i].value = element.value
                        self.numeric_registers[i].comment = element.comment
                        if element.id == 31:
                            print(f"Value of register 31 is: {element}")
                    print(f"Robot state is: {self.numeric_registers[30]}")

            else:
                print(
                    f"Error fetching numeric registers: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
        print("Finishing fetching numeric registers...")

    def fetch_string_registers(self):
        print("Fetching string registers...")
        string_url = f'http://{self.ip_address}/karel/ComGet?sFc=30'
        try:
            response = requests.get(string_url)
            if response.status_code == 200:
                with self.lock:
                    new_values = self.parse_string_registers(response.text)
                    for i, value in enumerate(new_values):
                        self.string_registers[i] = value
            else:
                print(
                    f"Error fetching string registers: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
        print(f"Finished fetching string registers...")

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

    @staticmethod
    def parse_numeric_registers(response_text):
        return parse_html_content_onto_numeric_registers(response_text)

    @staticmethod
    def parse_string_registers(response_text):
        return parse_html_content_onto_string_registers(response_text)
    
    def get_numeric_registers(self):
        return self.numeric_registers
