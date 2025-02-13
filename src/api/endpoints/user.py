"""
API requests with prefix /user.
There are function to deal with user: auth and etc.
"""
from fastapi import APIRouter, Depends

from models import User
from schemas import UserOut

from .. import dependencies

router = APIRouter()


@router.get("/me", description="Request to get current user profile.")
async def get_my_profile(user: User = Depends(dependencies.get_current_user)) -> UserOut:
    return user
