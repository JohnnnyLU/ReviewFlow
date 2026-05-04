import re

from pydantic import (
    BaseModel,
    Field,
    EmailStr,
    field_validator,
)

class BusinessSchema(BaseModel):
    business_name:  str = Field(..., min_length=3, max_length=100)
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=100)

    @field_validator('password')
    def validate_password(cls, v: str) -> str:
        if not re.search(r'[a-zA-Z]', v):
            raise ValueError('The password must contain Latin characters.')
        if not re.search(r'[A-Z]', v):
            raise ValueError('The password must contain at least one uppercase letter.')
        if not re.search(r'[a-z]', v):
            raise ValueError('The password must contain at least one lowercase letter.')
        if not re.search(r'\d', v):
            raise ValueError('The password must contain at least one digit.')
        if not re.search(r'[!@#$%^&*(),.?\':{}|<>]', v):
            raise ValueError('The password must contain at least one special character.')
        if ' ' in v:
            raise ValueError('The password cannot contain spaces.')
        return v

class LoginSchema(BaseModel):
    email: EmailStr
    password: str