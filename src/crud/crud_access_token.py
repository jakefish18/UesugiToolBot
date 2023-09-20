"""
CRUD requests for access tokens.
"""
from sqlalchemy.orm import Session

from src.crud.base import CRUDBase
from src.models import AccessToken


class CRUDAcessToken(CRUDBase[AccessToken]):
    def __init__(self, Model: type[AccessToken]):
        super().__init__(Model)

    def get_by_token(self, db: Session, token: str) -> AccessToken:
        """
        Get access token info by token.

        Parameters:
            db: Session - db session to deal with.
            token: str - token.

        Returns:
            access_token: Access token - access token.
            None if there isn't such access token.
        """

        return db.query(AccessToken).filter(AccessToken.token == token).first()
