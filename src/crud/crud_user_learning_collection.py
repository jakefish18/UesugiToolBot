"""
CRUD requests for user learning collections.
"""
from typing import Type, Union

from sqlalchemy.orm import Session

from src.crud.base import CRUDBase
from src.models import LearningCard, UserLearningCollection


class CRUDUserLearningCollection(CRUDBase[UserLearningCollection]):
    def __init__(self, Model: type[LearningCard]):
        super().__init__(Model)
