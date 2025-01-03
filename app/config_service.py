import logging
import os
import yaml

logger = logging.getLogger(__name__)


class ConfigurationError(Exception):
    pass

class ConfigService:
    def __init__(self):
        environment = os.environ.get('FLASK_ENV', 'development')
        logger.info(f"Environment is: {environment}")
        config_file = 'config_prod.yml' if environment == 'production' else 'config_dev.yml'
        self.config_data = self._load_config_file(config_file)

    def _load_config_file(self, config_file):
        if not os.path.exists(config_file):
            raise FileNotFoundError(f"The configuration file {config_file} does not exist.")

        with open(config_file, 'r') as file:
            return yaml.safe_load(file)


    def get(self, property_path):
        keys = property_path.split('.')
        value = self.config_data
        for key in keys:
            if value is None or key not in value:
                raise ConfigurationError(f"Configuration not found for path: {property_path}")
            value = value[key]
        return value
