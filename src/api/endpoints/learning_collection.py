"""
API requests with prefix /learning_collection.
"""
from fastapi import APIRouter, Depends
from models import User

from .. import dependencies

router = APIRouter()


@router.get("/all", description="Request to get all learning collections.")
async def get_all(*, user: User = Depends(dependencies.get_current_user)):
    """
    Getting all user learning collection.

    Parameters:
        db: Session - SQLAlchemy session to database, initializing in dependency injection.
        redis: Redis - Redis session for caching, using to store access token with TTL.
        user: User - dependency injection, which gets user access token from cookies.

    Returns:
        Json.
    """
    response_json = []
    print(user.learning_collections)
    for user_learning_collection in user.learning_collections:
        response_json.append(
            [user_learning_collection.learning_collection.id, user_learning_collection.learning_collection.name]
        )
    return response_json
