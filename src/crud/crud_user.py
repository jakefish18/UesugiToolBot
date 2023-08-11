"""
CRUD requests for user.
"""
from typing import Union

from sqlalchemy.orm import Session

from src.crud.base import CRUDBase
from src.models import LearningSession, User


class CRUDUser(CRUDBase[User]):
    def __init__(self, Model: type[User]):
        super().__init__(Model)

    def get_by_telegram_id(self, db: Session, telegram_id: int) -> Union[User, None]:
        """
        Getting user by telegram id.

        Parameters:
            telegram_id: int - telegram id of the user to get user id.

        Returns:
            user: User - user.
            None if there isn't user with the same telegram id.
        """
        return db.query(User).filter(User.telegram_id == telegram_id).first()

    def set_learning_session(self, db: Session, user: User, learning_session: LearningSession) -> User:
        """
        Setting user learning session.

        Parameters:
            user: User - the user whose session to set.
            learning_session: LearningSession - learning session.

        Returns:
            nothing
        """
        user.learning_session_id = learning_session.id
        db.commit()
        db.refresh(user)
        return user

    def is_user_telegram_id(self, db: Session, telegram_id: int) -> bool:
        """
        Checking if there is a user with given telegram_id.

        Arguments:
            telegram_id int - telegram_id to check.

        Returns:
            Bool flag which equals to True if there is user with the same telegram id in database
        """
        result = self.get_user_by_telegram_id(db, telegram_id)
        return bool(result)
