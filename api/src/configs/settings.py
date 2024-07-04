from enum import Enum

from pydantic_settings import BaseSettings, SettingsConfigDict


class EnvMode(Enum):
    DEV = 1
    TEST = 2
    PROD = 3


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    DATABASE_URL: str
    SECRET_KEY: str
    DEBUG: bool
    ENV_MODE: EnvMode | int
    MARIADB_USER: str
    MARIADB_ROOT_PASSWORD: str
    MARIADB_PASSWORD: str
    MARIADB_DATABASE: str


settings = Settings()  # type: ignore
