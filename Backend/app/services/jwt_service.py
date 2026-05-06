from app.models import Business
from app.core.config import settings

from jose import jwt


class JWTService:
    def __init__(self):
        self.algorithm = settings.auth_jwt.algorithm

    def encode(
            self,
            payload,
            private_key: str,
    ):
        encoded = jwt.encode(
            payload,
            private_key,
            self.algorithm,
        )
        return encoded

    def decode(
            self,
            token,
            secret_key,

    ):
        decoded = jwt.decode(
            token,
            secret_key,
            algorithms=[self.algorithm],
        )
        return decoded