import os
import json
from pydantic import BaseModel

class TelegramSettings(BaseModel):
    token: str

class FilePaths(BaseModel):
    ai: str
    ai_product: str

class URLs(BaseModel):
    ai: str
    ai_product: str

class AppConfig(BaseModel):
    telegram: TelegramSettings
    files: FilePaths
    sites: URLs

def load_config() -> AppConfig:
    config_path = os.environ.get("CONFIG_PATH", "configs/bot_config.json")
    with open(config_path, encoding="utf-8") as f:
        raw = json.load(f)
    return AppConfig(**raw)