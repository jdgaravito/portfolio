'''Imports for the config file'''
import logging
import os
from functools import lru_cache
from pydantic import AnyUrl
from pydantic_settings import BaseSettings

log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    '''App settings'''
    environment: str = os.getenv("ENVIRONMENT", "dev")
    testing: bool = os.getenv("TESTING", "0") == "1"
    database_url: AnyUrl = os.environ.get("DATABASE_URL")


@lru_cache()
def get_settings() -> BaseSettings:
    '''Get the app settings from the environment variables.'''
    log.info("Loading config settings from the environment...")
    return Settings()