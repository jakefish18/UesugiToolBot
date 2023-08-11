"""
CRUD requests for learning session cards.
"""
from typing import Type, Union

from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import func

from src.crud.base import CRUDBase
from src.models import LearningSessionCard


class CRUDLearningSessionCard(CRUDBase[LearningSessionCard]):
    def __init__(self, Model: type[LearningSessionCard]):
        super().__init__(Model)
