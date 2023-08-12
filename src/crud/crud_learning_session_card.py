"""
CRUD requests for learning session cards.
"""
from typing import Type, Union

from sqlalchemy import and_
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import func

from src.crud.base import CRUDBase
from src.models import LearningSession, LearningSessionCard


class CRUDLearningSessionCard(CRUDBase[LearningSessionCard]):
    def __init__(self, Model: type[LearningSessionCard]):
        super().__init__(Model)

    def get_answer_card(self, db: Session, learning_session: LearningSession):
        """
        Getting random answer card, where is_passed field equals False.

        Parameters:
            db: Session - db session to deal with.

        Returns:
            answer_card: LearningSessionCard - answer card.
        """
        return (
            db.query(LearningSessionCard)
            .filter(
                and_(
                    LearningSessionCard.is_passed == False,
                    LearningSessionCard.learning_session_id == learning_session.id,
                )
            )
            .order_by(func.random())
            .first()
        )

    def get_extra_cards(
        self, db: Session, answer_card: LearningSessionCard, learning_session: LearningSession, count: int
    ):
        """
        Getting extra cards for another answer options.

        Parameters:
            db: Session - db session to deal with.
            count: int - count of cards.

        Returns:
            extra_cards: list[LearningSessionCard] - extra cards.
        """
        return (
            db.query(LearningSessionCard)
            .order_by(func.random())
            .filter(
                and_(
                    LearningSessionCard.id != answer_card.id,
                    LearningSessionCard.learning_session_id == learning_session.id,
                )
            )
            .limit(count)
            .all()
        )
