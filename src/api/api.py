"""
Including every router from /endpoints.
app: FastAPI - main variable for backend launching.
"""

from fastapi import FastAPI

from .endpoints import learning_collection, user

api = FastAPI()
api.include_router(user.router, prefix="/user", tags=["user"])
api.include_router(learning_collection.router, prefix="/learning_collection", tags=["learning_collection"])
