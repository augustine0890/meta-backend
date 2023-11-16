from typing import Optional

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ENV_STAGE: Optional[str] = "dev" 
    class Config:
        env_file = ".env"

class GlobalConfig(BaseSettings):
    DATABASE_URL: str = "sqlite:///default.db"  # Default value for DATABASE_URL
    DB_FORCE_ROLL_BACK: bool = False

    class Config(Settings.Config):
        pass

class DevSettings(GlobalConfig):
    class Config(Settings.Config):
        env_prefix = "DEV_"


class ProdSettings(GlobalConfig):
    class Config(Settings.Config):
        env_prefix = "PROD_"


class TestSettings(GlobalConfig):
    DATABASE_URL: str = "sqlite:///test.db"
    DB_FORCE_ROLL_BACK: bool = True

    class Config(Settings.Config):
        env_prefix = "TEST_"


def get_settings(environment: str) -> Settings:
    if environment == "prod":
        return ProdSettings()
    elif environment == "test":
        return TestSettings()
    else:
        # Default to development settings
        return DevSettings()

# Instantiate the settings based on the current environment
settings = get_settings(Settings().ENV_STAGE)