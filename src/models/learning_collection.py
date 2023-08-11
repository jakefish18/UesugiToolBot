"""Learning collection SQLAlchemy model."""
import datetime

from sqlalchemy import BigInteger, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.db import Base


class LearningCollection(Base):
    __tablename__ = "learning_collections"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, unique=True)
    owner_id = Column(BigInteger, ForeignKey("users.id"), index=True)
    added_at = Column(DateTime, default=datetime.datetime.utcnow)

    owner = relationship("User", back_populates="learning_collections", foreign_keys=[owner_id])
    cards = relationship("LearningCard", back_populates="learning_collection")
    learning_sessions = relationship("LearningSession", back_populates="learning_collection")
