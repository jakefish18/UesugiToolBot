"""
API requests with prefix /user.
There are function to deal with user: auth and etc.
"""
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query, Response, status
from fastapi.responses import RedirectResponse
from redis import Redis
from sqlalchemy.orm import Session

from core import security
from crud import crud_access_token, crud_auth_token, crud_user
from models import AccessToken, User
from schemas import UserOut

from .. import dependencies

router = APIRouter()


@router.get("/me", description="Request to get current user profile.")
async def get_my_profile(user: User = Depends(dependencies.get_current_user)) -> UserOut:
    return user
