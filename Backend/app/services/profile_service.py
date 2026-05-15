from app.models import Business
from app.repositories.profile_repo import ProfileRepository
from app.schemas.profile import UpdateProfileSchema, ProfileResponseSchema

class ProfileService:
    def __init__(self, repo: ProfileRepository):
        self.repo = repo

    async def update_profile(
        self,
        business: Business,
        schema: UpdateProfileSchema
    ) -> ProfileResponseSchema:

        update_data = schema.model_dump(
            exclude_unset=True,
            exclude_none=False
        )

        if not update_data:
            raise ValueError('Empty update payload')

        updated_profile = await self.repo.update_profile(
            business_id=business.id,
            data=update_data
        )

        return ProfileResponseSchema.model_validate(
            updated_profile,
            from_attributes=True
        )