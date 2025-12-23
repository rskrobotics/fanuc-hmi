import os
from functools import lru_cache
from pathlib import Path

import yaml
from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class RobotConfig(BaseModel):
    ip: str = "172.18.1.201"


class DisplayedRegisters(BaseModel):
    numeric: list[int] = [10, 31, 89, 90, 21]
    string: list[int] = []


class FetchIntervals(BaseModel):
    seconds_numeric: int = 1
    seconds_string: int = 60


class TriggerConfig(BaseModel):
    value: int = 1
    revert_value: int = 0
    register_id: int = 10
    revert_delay_seconds: int = 5


class Settings(BaseSettings):
    robot: RobotConfig = RobotConfig()
    displayed_registers: DisplayedRegisters = DisplayedRegisters()
    fetch_intervals: FetchIntervals = FetchIntervals()
    quote_api_url: str = (
        "http://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=json"
    )
    cache_timeout_seconds: int = 3600
    trigger: TriggerConfig = TriggerConfig()
    mock_robot: bool = False

    model_config = SettingsConfigDict(env_prefix="", extra="ignore")


def load_yaml_config() -> dict:
    config_path = Path(__file__).parent / "config.yml"
    if config_path.exists():
        with open(config_path) as f:
            return yaml.safe_load(f) or {}
    return {}


@lru_cache
def get_settings() -> Settings:
    yaml_config = load_yaml_config()

    # Check for MOCK_ROBOT env var (overrides yaml)
    mock_robot = os.environ.get("MOCK_ROBOT", "").lower() in ("true", "1", "yes")
    if mock_robot:
        yaml_config["mock_robot"] = True

    return Settings(**yaml_config)
