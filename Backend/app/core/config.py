from pathlib import Path
from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent.parent

class Auth(BaseModel):
    # JWT
    jwt_secret_key: str
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    refresh_token_expire_days: int = 14

    # Google
    google_client_id: str
    google_client_secret: str
    google_redirect_uri: str

class Settings(BaseSettings):
    DB_HOST: str
    DB_SYNC_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    def _build_db_url(self, conn_type: str, host: str) -> str:
        return (
            f'postgresql+{conn_type}://'
            f'{self.DB_USER}:{self.DB_PASS}'
            f'@{host}:{self.DB_PORT}/{self.DB_NAME}'
        )

    @property
    def db_url(self) -> str:
        return self._build_db_url('asyncpg', self.DB_HOST)

    @property
    def sync_db_url(self) -> str:
        return self._build_db_url('psycopg', self.DB_SYNC_HOST)

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / '.env'
    )

    auth_jwt: Auth = Auth()

settings = Settings()