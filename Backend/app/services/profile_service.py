from fastapi import HTTPException, status

from app.models import Business
from app.repositories import ProfileRepository, BusinessRepository
from app.schemas.profile import UpdateProfileSchema, ProfileResponseSchema


class ProfileService:
    def __init__(
            self,
            profile_repo: ProfileRepository,
            business_repo: BusinessRepository
    ):
        self.profile_repo = profile_repo
        self.business_repo = business_repo

    async def get_profile(
        self,
        business: Business,
    ) -> ProfileResponseSchema:

        business = await self.business_repo.get_by_id(business.id)

        if not business:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Business found'
            )

        return ProfileResponseSchema.model_validate(
            business,
            from_attributes=True,
        )

    async def update_profile(
        self,
        business: Business,
        schema: UpdateProfileSchema
    ) -> ProfileResponseSchema:

        update_data = schema.model_dump(
            exclude_unset=True,
        )

        if not update_data:
            raise ValueError('Empty update payload')

        updated_profile = await self.profile_repo.update_profile(
            business_id=business.id,
            data=update_data
        )

        return ProfileResponseSchema.model_validate(
            updated_profile,
            from_attributes=True
        )