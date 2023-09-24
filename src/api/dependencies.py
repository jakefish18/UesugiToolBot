"""
Dependencies for FastAPI dependency injection system.
"""

from typing import Annotated, Generator

from fastapi import Cookie, Depends, HTTPException, status
from redis import Redis
from sqlalchemy.orm import Session

from src import cache_db
from src.crud import crud_access_token, crud_user
from src.db import SessionLocal
from src.models import AccessToken, User


def get_db() -> Generator:
    """
    This dependency injection used for creating db session.
    Db session closes after FastAPI query completion.

    Parameters:
        Nothing.

    Returns:
        db: Session - database session.
    """
    try:
        db = SessionLocal()
        return db
    finally:
        db.close()


def get_redis() -> Generator:
    """
    This dependency injection used for creating redis session.
    Redis session closes after FastAPI query completion.

    Parameters:
        Nothing.

    Returns:
        redis: Redis - redis session.
    """
    try:
        print("GETTING")
        redis: Redis = cache_db.open()
        yield redis
    finally:
        redis.close()


def get_current_user(access_token: Annotated[str, Cookie()], db: Session = Depends(get_db)) -> User:
    """
    This dependency injection used for getting user, which has sent requests with access token.
    Token must be stored in cookies.

    Parameters:
        access_token: Annotated[str, Cookie()] - access token from cookie.
        db: Session - SQLAlchemy session to database, initializing in dependency injection.

    Returns:
        user: models.User - user sqlalchemy model.
        HTTPExecption(401) if invalid access token.
    """
    access_token_data: AccessToken = crud_access_token.get_by_token(db, access_token)

    if not access_token_data:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="Invalid access token.")

    user: User = crud_user.get(db, access_token_data.user_id)

    if not user:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Invalid credentials")

    return user
