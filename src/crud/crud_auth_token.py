from typing import Union

from redis import Redis

from core import settings
from models import User


class CRUDAuthToken:
    def __init__(self) -> None:
        pass

    def create(self, redis: Redis, user: User, token: str) -> str:
        """
        Creating email confirm token in redis database.

        Parameters:
            redis: Redis - redis database session to deal with.
            user_id: int - user id to whom crete auth token.

        Returns:
            auth_token: str - the same value as passed token.
        """
        redis.set(token, user.id, ex=settings.AUTH_TOKEN_EXPIRING_TIME)
        return token

    def verify(self, redis: Redis, auth_token: str) -> Union[int, None]:
        """
        Verifying user auth token.

        Parameters:
            redis: Redis - redis database session to deal with.
            auth_token: str - token to check.

        Returns:
            None - if there isn't such token.
            user_id - id of user to whom auth token belongs.
        """
        user_id: int = redis.get(auth_token)
        if not user_id:
            return None

        redis.delete(auth_token)
        return user_id
