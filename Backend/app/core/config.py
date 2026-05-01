from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DB_URL: str
    SYNC_DB_URL: str

    class Config:
        env_file = ".env"

settings = Settings()