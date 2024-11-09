"""
CRUD requests for user learning collections.
"""
from typing import Type, Union

from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models import LearningCard, UserLearningCollection


class CRUDUserLearningCollection(CRUDBase[UserLearningCollection]):
    def __init__(self, Model: type[UserLearningCollection]):
        super().__init__(Model)
