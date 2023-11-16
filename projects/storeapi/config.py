import os
from functools import lru_cache
from typing import Optional

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DEBUG: bool = False
    TESTING: bool = False
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "DEV")
    DATABASE_URL: Optional[str] = os.getenv("DATABASE_URL", "sqlite:///data.db")
    DB_FORCE_ROLL_BACK: bool = False


class DevConfig(Settings):
    DEBUG: bool = True


class TestConfig(Settings):
    DEBUG: bool = True
    TESTING: bool = True
    DATABASE_URL: str = "sqlite:///test.db"
    DB_FORCE_ROLL_BACK: bool = True


class FactoryConfig:
    """Returns a config instance depends on the ENV_STATE variable."""

    def __init__(self, environment: Optional[str] = "DEV"):
        self.environment = environment

    def __call__(self):
        if self.environment == "TEST":
            return TestConfig()
        elif self.environment == "PROD":
            return Settings()
        return DevConfig()


@lru_cache()
def get_configuration():
    return FactoryConfig(Settings().ENVIRONMENT)()


print("Getting configuration")
config = get_configuration()
