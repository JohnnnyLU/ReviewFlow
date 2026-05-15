from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.services import AuthService

from app.schemas import BusinessSchema, LoginSchema, TokenResponse

from app.api.deps import get_auth_service

from app.core.database_helper import get_db


router = APIRouter()

@router.post('/register')
async def register_business(
    data: BusinessSchema,
    session: AsyncSession = Depends(get_db),
    auth_service: AuthService = Depends(get_auth_service),
):
    return await auth_service.register(session, data)

@router.post('/login', response_model=TokenResponse)
async def login_business(
    data: LoginSchema,
    session: AsyncSession = Depends(get_db),
    auth_service: AuthService = Depends(get_auth_service),
):
    return await auth_service.login(
        email=data.email,
        password=data.password,
        session=session
    )