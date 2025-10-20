from pydantic_settings import BaseSettings
import os
from functools import lru_cache


class Settings(BaseSettings):
    APP_NAME: str = os.getenv('APP_NAME', '')
    APP_VERSION: str = os.getenv('APP_VERSION', '')


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()
