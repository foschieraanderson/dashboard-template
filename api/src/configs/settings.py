from enum import Enum

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import computed_field


class EnvMode(Enum):
    DEV = 1
    TEST = 2
    PROD = 3


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    SECRET_KEY: str
    DEBUG: bool
    ENV_MODE: EnvMode | int
    MARIADB_USER: str
    MARIADB_ROOT_PASSWORD: str
    MARIADB_PASSWORD: str
    MARIADB_DATABASE: str
    MARIADB_PORT: int
    MARIADB_HOST: str

    @computed_field  # type: ignore[misc]
    @property
    def SQLALCHEMY_DATABASE_URI(self) -> str:
        return f"mariadb+asyncmy://{self.MARIADB_USER}:{self.MARIADB_ROOT_PASSWORD}@{self.MARIADB_HOST}:{self.MARIADB_PORT}/{self.MARIADB_DATABASE}"


settings = Settings()  # type: ignore
