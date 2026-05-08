from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.services import JWTService

from app.schemas import BusinessSchema, LoginSchema, TokenResponse

from app.api.deps import (
    get_db,
    get_auth_service,
    get_jwt_service
)

router = APIRouter()

@router.post('/register')
async def register_business(
    data: BusinessSchema,
    session: AsyncSession = Depends(get_db),
    auth_service: JWTService = Depends(get_auth_service),
):
    return await auth_service.register(session, data)

@router.post('/login', response_model=TokenResponse)
async def login_business(
    data: LoginSchema,
    session: AsyncSession = Depends(get_db),
    auth_service: AuthService = Depends(get_auth_service),
):
    try:
        token = await auth_service.authentificate(data.email, data.password, session)


    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid credentials',
        )
