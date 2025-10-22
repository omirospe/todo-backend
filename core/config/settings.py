from pydantic_settings import BaseSettings
import os
from functools import lru_cache


class Settings(BaseSettings):
    APP_NAME: str = os.getenv('APP_NAME', '')
    APP_VERSION: str = os.getenv('APP_VERSION', '')

    DB_USER: str = os.getenv('DB_USER', 'postgres')
    DB_PASSWORD: str = os.getenv('DB_PASSWORD', 'postgres')
    DB_SERVER: str = os.getenv('DB_SERVER', 'localhost')
    DB_PORT: str = os.getenv('DB_PORT', '5432')
    DB_NAME: str = os.getenv('DB_NAME', 'dev')


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()
