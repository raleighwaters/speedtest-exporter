import logging

from pydantic import Field
from pydantic_settings import BaseSettings

logger = logging.getLogger(__name__)

class Settings(BaseSettings):
    SPEEDTEST_INTERVAL: int = Field(default=600, description="Interval in seconds between speedtest runs")
    TEST_MODE: bool = Field(default=False, description="Use test mode with mock data")

    class Config:
        env_file = ".env"
        case_sensitive = False

    def log_settings(self):
        logger.debug("Application settings:")
        for key, value in self.model_dump().items():
            logger.debug(f"   {key} = {value}")

# Global settings instance
settings = Settings()
