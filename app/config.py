import os
from typing import List
from pydantic_settings import BaseSettings, SettingsConfigDict
import os
from loguru import logger


class Settings(BaseSettings):
    FORMAT_LOG: str = "{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}"
    LOG_ROTATION: str = "10 MB"
    bot_token: str
    admins = list
    db_url = str
    host_redis = str
    port_redis = int
    password_redis = str

    model_config = SettingsConfigDict(
        env_file=os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env"),
        extra="ignore"
    )


settings = Settings()
logger.info(settings.ADMINS)