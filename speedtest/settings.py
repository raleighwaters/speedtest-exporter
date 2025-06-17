from pydantic import Field
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SPEEDTEST_INTERVAL: int = Field(default=600, description="Interval in seconds between speedtest runs")
    TEST_MODE: bool = Field(default=False, description="Use test mode with mock data")

    class Config:
        env_file = ".env"
        case_sensitive = False

# Global settings instance
settings = Settings()
