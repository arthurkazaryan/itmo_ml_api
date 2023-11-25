from pydantic import AnyUrl, Field
from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

    API_PORT: int = Field(ge=1024, lt=65536)
    DATABASE_URL: AnyUrl


app_settings = AppSettings()
