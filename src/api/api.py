"""
Including every router from /endpoints.
app: FastAPI - main variable for backend launching.
"""

from fastapi import FastAPI

from .endpoints import auth, learning_collection, user

api = FastAPI()
api.include_router(auth.router, prefix="/auth", tags=["auth"])
api.include_router(learning_collection.router, prefix="/learning_collections", tags=["learning_collection"])
api.include_router(user.router, prefix="/users", tags=["user"])