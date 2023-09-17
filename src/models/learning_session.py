"""Learning session SQLAlchemy model."""
import datetime

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship

from src.db import Base


class LearningSession(Base):
    __tablename__ = "learning_sessions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), index=True, unique=True)
    learning_collection_id = Column(Integer, ForeignKey("learning_collections.id", ondelete="CASCADE"))
    is_active = Column(Boolean, default=True)
    started_at = Column(DateTime, default=datetime.datetime.utcnow)

    user = relationship("User", back_populates="learning_session", foreign_keys=[user_id], uselist=False)
    learning_collection = relationship(
        "LearningCollection", back_populates="learning_sessions", foreign_keys=[learning_collection_id], uselist=False
    )
    cards = relationship("LearningSessionCard", back_populates="learning_session")
