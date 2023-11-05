import yaml
import os

class ConfigService:
    def __init__(self, config_file='config.yml'):
        self.config_file = config_file
        self.config_data = self._load_config_file()

    def _load_config_file(self):
        if not os.path.exists(self.config_file):
            raise FileNotFoundError(f"The configuration file {self.config_file} does not exist.")

        with open(self.config_file, 'r') as file:
            return yaml.safe_load(file)
        

    def get(self, property_path, default=None):
        keys = property_path.split('.')
        value = self.config_data
        for key in keys:
            if value is not None and key in value:
                value = value[key]
            else:
                return default
        return value

