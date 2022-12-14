from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "EPG_FastApi_Calc"
    hello_text: str = "Hello world"
    val_regex: str = r'^[0-9\s\.\/\*\+\-\(\)]*$'

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()


settings = get_settings()
