"""
CRUD requests for user learning collections.
"""
from typing import Type, Union

from sqlalchemy.orm import Session
from sqlalchemy import and_

from crud.base import CRUDBase
from models import LearningCard, UserLearningCollection, LearningCollection, User


class CRUDUserLearningCollection(CRUDBase[UserLearningCollection]):
    def __init__(self, Model: type[UserLearningCollection]):
        super().__init__(Model)

    def get_by_user_and_learning_collection(self, db: Session, user: User, learning_collection: LearningCollection) -> UserLearningCollection:
        return db.query(UserLearningCollection).filter(and_(
            UserLearningCollection.user_id == user.id,
            UserLearningCollection.learning_collection_id == learning_collection.id,
        )).first()

    def is_exists(self, db: Session, user: User, learning_collection: LearningCollection) -> bool:
        return self.get_by_user_and_learning_collection(db, user, learning_collection) != None