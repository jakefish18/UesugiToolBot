"""
CRUD requests for user.
"""
from typing import Type, Union

from sqlalchemy import and_
from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models import LearningCollection, User


class CRUDLearningCollection(CRUDBase[LearningCollection]):
    def __init__(self, Model: type[LearningCollection]):
        super().__init__(Model)

    def get_by_name(self, db: Session, user: User, name: str) -> Union[LearningCollection, None]:
        """
        Get learning collection by learning collection name.

        Parameters:
            db: Session - db session to deal with.
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

    def get_by_name_and_author_id(self, db: Session, name: str, author_id: int) -> Union[LearningCollection, None]:
        """
        Get learning collection by learning collection name and author id.
        There won't be any result if learning collection is_public field equals False!!!

        Parameters:
            db: Session - db session to deal with.
            name: str - name of learning collection.
            author_id: int - author id.

        Returns:
            learning_collection: LearningCollection - learning collection.
            None if there isn't such learning collection.
        """
        return (
            db.query(LearningCollection)
            .filter(and_(LearningCollection.name == name, LearningCollection.owner_id == author_id))
            .first()
        )

    def update_to_public(self, db: Session, learning_collection: LearningCollection) -> Union[LearningCollection, None]:
        """
        Updating learning collection.
        Setting is_public flag to true and changing name to unique name in database.

        Parameters:
            db: Session - db session to deal with.
            learning_collection: LearningCollection - learning collection SQLAlchemy model to update.

        Returns:
            learning_collection: LearningCollection - updated learning_collection.
            None if learning_collection is_public flag already equals to True.
        """
        if learning_collection.is_public:  # Handling error, when learning collection is already public.
            return

        # Updating learning collection.
        learning_collection.is_public = True
        db.commit()
        db.refresh(learning_collection)
        return learning_collection
