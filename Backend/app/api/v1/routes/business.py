from fastapi import APIRouter, Depends
from app.api.deps import get_current_business
from app.models import Business

router = APIRouter()

# test
@router.get('/me')
async def me(business: Business = Depends(get_current_business)):
    return business