"""
Including every router from /endpoints.
app: FastAPI - main variable for backend launching.
"""

from fastapi import APIRouter

from .endpoints import user

api_router = APIRouter()
api_router.include_router(user.router, prefix="/user", tags=["user"])
