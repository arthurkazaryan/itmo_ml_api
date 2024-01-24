from pydantic import AnyUrl, Field
from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

    PROJECT_NAME: str
    BACKEND_CORS_ORIGINS: list = []

    API_PORT: int = Field(ge=1024, lt=65536)
    DATABASE_URL: AnyUrl
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 30

    PAGE: int = 1
    PAGE_SIZE: int = 20
    ORDERING: str = "-id"

    # date
    DATETIME_FORMAT: str = "%Y-%m-%dT%H:%M:%S"
    DATE_FORMAT: str = "%Y-%m-%d"


app_settings = AppSettings()
