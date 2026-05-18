from urllib.parse import urlparse

from pydantic import BaseModel, Field, field_validator, EmailStr, ConfigDict


ALLOWED_DOMAINS = {
    'google.com',
    'maps.google.com',
    'yandex.ru',
    'maps.yandex.ru',
    '2gis.ru',
    'maps.2gis.ru',
}

def validate_review_urls(v: str) -> str:
    parsed = urlparse(v)

    if parsed.scheme not in ('http', 'https'):
        raise ValueError('Invalid URL scheme')

    domain = parsed.netloc.lower().replace('www.', '')

    if not any(
        domain == allowed
        or domain.endswith(f'.{allowed}')
        for allowed in ALLOWED_DOMAINS
    ):
        raise ValueError('Unsupported domain')

    return v

def validate_regular_url(v: str) -> str:
    parsed = urlparse(v)

    if parsed.scheme not in ('http', 'https'):
        raise ValueError('Invalid URL scheme')

    return v


class ProfileResponseSchema(BaseModel):
    id: int
    business_name: str
    token: str
    avatar_url: str | None

    google_review_url: str | None
    yandex_review_url: str | None
    twogis_review_url: str | None

class UpdateProfileSchema(BaseModel):
    model_config = ConfigDict(extra='forbid')

    business_name: str | None = Field(
        default=None,
        min_length=3,
        max_length=128,
    )

    avatar_url: str | None = Field(
        default=None,
    )

    google_review_url: str | None = Field(
        default=None,
    )

    yandex_review_url: str | None = Field(
        default=None,
    )

    twogis_review_url: str | None = Field(
        default=None,
    )

    @field_validator('avatar_url')
    @classmethod
    def validate_avatar_url(cls, v: str | None):
        if v is None:
            return v

        return validate_regular_url(v)

    @field_validator(
        'google_review_url',
        'yandex_review_url',
        'twogis_review_url',
    )
    @classmethod
    def validate_review_urls(cls, v: str | None):
        if v is None:
            return v

        return validate_review_urls(v)