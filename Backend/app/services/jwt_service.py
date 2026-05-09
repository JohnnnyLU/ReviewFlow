from app.models import Business
from app.core.config import settings

from jose import jwt, JWTError, ExpiredSignatureError

from datetime import datetime, timedelta, timezone
from fastapi import HTTPException, status


class JWTService:
    def __init__(self):
        self.algorithm = settings.auth_jwt.algorithm
        self.secret_key = settings.auth_jwt.secret_key

    def create_access_token(self, data: dict) -> str:
        to_encode = data.copy()
        expire = datetime.now(timezone.utc) + timedelta(minutes=settings.auth_jwt.access_token_expire_minutes)

        to_encode.update({
            "exp": expire,
            "type": "access"
        })

        return self._encode(to_encode, self.secret_key)

    def create_refresh_token(self, data: dict) -> str:
        to_encode = data.copy()
        expire = datetime.now(timezone.utc) + timedelta(days=settings.auth_jwt.refresh_token_expire_days)

        to_encode.update({
            "exp": expire,
            "type": "refresh"
        })

        return self._encode(to_encode, self.secret_key)

    def _encode(self, payload: dict, key: str) -> str:
        return jwt.encode(
            payload,
            key,
            algorithm=self.algorithm,
        )

    def decode_token(self, token: str) -> dict:
        try:
            decoded = jwt.decode(
                token,
                self.secret_key,
                algorithms=[self.algorithm],
            )
            return decoded

        except ExpiredSignatureError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token has expired",
                headers={"WWW-Authenticate": "Bearer"},
            )
        except JWTError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )