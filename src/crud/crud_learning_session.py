"""
CRUD requests for learning sessions.
"""
from typing import Type, Union

from sqlalchemy.orm import Session

from src.crud.base import CRUDBase
from src.models import LearningSession, User


class CRUDLearningSession(CRUDBase[LearningSession]):
    def __init__(self, Model: type[LearningSession]):
        super().__init__(Model)
