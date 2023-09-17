"""Learning card SQLAlchemy model."""
import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.db import Base


class LearningCard(Base):
    __tablename__ = "learning_cards"

    id = Column(Integer, primary_key=True, index=True)
    learning_collection_id = Column(Integer, ForeignKey("learning_collections.id", ondelete="CASCADE"))
    question = Column(String)
    answer = Column(String)
    added_at = Column(DateTime, default=datetime.datetime.utcnow)

    learning_collection = relationship(
        "LearningCollection", back_populates="cards", foreign_keys=[learning_collection_id]
    )
    learning_sessions = relationship("LearningSessionCard", back_populates="card")
