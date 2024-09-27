import logging
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    OSRM_URL: str = "http://localhost:5001"
    LOG_LEVEL: str = "INFO"

    class Config:
        env_file = ".env"

settings = Settings()

# Configure logging
logging.basicConfig(
    level=settings.LOG_LEVEL,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)