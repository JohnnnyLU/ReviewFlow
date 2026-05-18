from fastapi import APIRouter, Depends

from app.api.deps import get_current_business, get_profile_service

from app.schemas.profile import UpdateProfileSchema, ProfileResponseSchema

from app.models import Business
from app.services import ProfileService

router = APIRouter()


@router.get(
    '/me',
    response_model = ProfileResponseSchema
)
async def get_profile(
    business: Business = Depends(get_current_business),
    service: ProfileService = Depends(get_profile_service),
):
    return await service.get_profile(business=business)

@router.patch(
    '/me',
    response_model = ProfileResponseSchema
)
async def update_profile(
    data: UpdateProfileSchema,
    business: Business = Depends(get_current_business),
    service: ProfileService = Depends(get_profile_service),
):
    return await service.update_profile(
        business=business,
        schema=data,
    )