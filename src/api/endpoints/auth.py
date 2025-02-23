"""
API requests with prefix /user.
There are function to deal with user: auth and etc.
"""
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query, Response, status
from fastapi.responses import RedirectResponse
from redis import Redis
from sqlalchemy.orm import Session

from core import security, settings
from crud import crud_access_token, crud_auth_token, crud_user
from models import AccessToken

from .. import dependencies

router = APIRouter()


@router.get("/login", description="Request for auth with token.")
async def auth_func(
    redis: Annotated[Redis, Depends(dependencies.get_redis)],
    auth_token: Annotated[str, Query(alias="auth-token", max_length=256, min_length=1)],
    response: Response,
    db: Session = Depends(dependencies.get_db),
):
    """
    Authing user with auth_token.

    Parameters:
        db: Session - SQLAlchemy session to database, initializing in dependency injection.
        redis: Redis - Redis session for caching, using to store access token with TTL.
        auth: Annotated[str, Query(alias="auth-token")] - query parameter with auth token string,
            query parameter name must be 'auth-token'

    Returns:
        JSON with access token info.
        HTTPException 401 - Invalid token. Token also might be expired.
    """
    print(auth_token)
    user_id = crud_auth_token.verify(redis, auth_token)

    # Exception if such auth token doesn't exist or expired.
    if not user_id:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="Invalid auth token")

    user = crud_user.get(db, user_id)

    access_token = AccessToken(user_id=user.id, token=security.create_token())
    access_token: AccessToken = crud_access_token.create(db, access_token)
    response = RedirectResponse(url=f"http://{settings.FRONTEND_DOMAIN}/#/shop")
    response.set_cookie("access_token", access_token.token, samesite="Lax", secure=False)
    return response


