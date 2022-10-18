from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Calculator"
    hello_text = "Hello world"
    val_regex: str = '^[0-9, /*+.-]+$'

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()


settings = get_settings()
