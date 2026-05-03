from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas import BusinessSchema
from app.services import AuthService

from app.api.deps import (
    get_db,
    get_auth_service,
)

router = APIRouter()

@router.post('/register')
async def register_business(
    data: BusinessSchema,
    session: AsyncSession = Depends(get_db),
    auth_service: AuthService = Depends(get_auth_service),
):
    return await auth_service.register(session, data)