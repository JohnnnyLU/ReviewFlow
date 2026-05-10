from fastapi import APIRouter, Request, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.services import AuthService
from .google import oauth
from app.api.deps import get_auth_service
from app.core.database_helper import get_db

router = APIRouter()

@router.get("/login")
async def google_login(request: Request):
    redirect_uri = request.url_for("google_callback")

    return await oauth.google.authorize_redirect(
        request=request,
        redirect_uri=redirect_uri,
    )


@router.get("/callback")
async def google_callback(
    request: Request,
    session: AsyncSession = Depends(get_db),
    auth_service: AuthService = Depends(get_auth_service),
):
    token = await oauth.google.authorize_access_token(request)

    business_info = token["userinfo"]

    return await auth_service.login_with_google(
        session=session,
        business_info=business_info,
    )