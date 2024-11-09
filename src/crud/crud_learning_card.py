"""
CRUD requests for learning cards.
"""
from typing import Type, Union

from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models import LearningCard


class CRUDLearningCard(CRUDBase[LearningCard]):
    def __init__(self, Model: type[LearningCard]):
        super().__init__(Model)
