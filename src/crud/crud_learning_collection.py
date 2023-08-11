"""
CRUD requests for user.
"""
from typing import Type, Union

from sqlalchemy import and_
from sqlalchemy.orm import Session

from src.crud.base import CRUDBase
from src.models import LearningCollection, User


class CRUDLearningCollection(CRUDBase[LearningCollection]):
    def __init__(self, Model: type[LearningCollection]):
        super().__init__(Model)

    def get_by_name(self, db: Session, user: User, name: str) -> Union[LearningCollection, None]:
        """
        Get learning collection by learning collection name.

        Parameters:
            name: str - name of learning collection.

        Returns:
            learning_collection: LearningCollection - learning collection.
            None if there isn't such learning collection.
        """
        return (
            db.query(LearningCollection)
            .filter(and_(LearningCollection.name == name, LearningCollection.owner_id == user.id))
            .first()
        )
