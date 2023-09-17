"""Learning session card SQLAlchemy model."""
import datetime

from sqlalchemy import Boolean, Column, ForeignKey, Integer, DateTime
from sqlalchemy.orm import relationship

from src.db import Base


class LearningSessionCard(Base):
    __tablename__ = "learning_session_cards"

    id = Column(Integer, primary_key=True, index=True)
    learning_session_id = Column(Integer, ForeignKey("learning_sessions.id", ondelete="CASCADE"), index=True)
    card_id = Column(Integer, ForeignKey("learning_cards.id", ondelete="CASCADE"))
    is_passed = Column(Boolean, default=False)

    learning_session = relationship("LearningSession", back_populates="cards", foreign_keys=[learning_session_id])
    card = relationship("LearningCard", back_populates="learning_sessions", foreign_keys=[card_id])
