"""
CRUD requests for learning sessions.
"""
from typing import Type, Union

from sqlalchemy import and_
from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models import LearningSession, User


class CRUDLearningSession(CRUDBase[LearningSession]):
    def __init__(self, Model: type[LearningSession]):
        super().__init__(Model)

    def get_user_session(self, db: Session, user: User) -> Union[LearningSession, None]:
        """
        Get user session by user.

        Parameters:
            db: Sessions - db session to deal with.
            user: User - user whoose session to get.

        Returns:
            learning_session: LearningSession - learning session.
            None if user hasn't sessions.
        """
        return (
            db.query(LearningSession)
            .filter(and_(LearningSession.user_id == user.id, LearningSession.is_active == True))
            .first()
        )
