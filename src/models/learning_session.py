"""Learning session SQLAlchemy model."""
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from src.db import Base


class LearningSession(Base):
    __tablename__ = "learning_sessions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True, unique=True)
    learning_collection_id = Column(Integer, ForeignKey("learning_collections.id"))

    user = relationship("User", back_populates="learning_session", foreign_keys=[user_id])
    learning_collection = relationship(
        "LearningCollection", back_populates="learning_sessions", foreign_keys=[learning_collection_id]
    )
    cards = relationship("LearningSessionCard", back_populates="learning_session")
