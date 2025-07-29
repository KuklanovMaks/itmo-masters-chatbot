from pydantic import BaseModel


class TelegramSettings(BaseModel):
    token: str


class AppSettings(BaseModel):
    telegram: TelegramSettings


def load_config() -> AppSettings:
    import os
    import json
    config_path = os.getenv("CONFIG_PATH", "config.json")
    with open(config_path, encoding="utf-8") as f:
        data = json.load(f)
    return AppSettings(**data)