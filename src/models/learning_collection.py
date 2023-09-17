"""Learning collection SQLAlchemy model."""
import datetime

from sqlalchemy import (
    BigInteger,
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship

from src.db import Base


class LearningCollection(Base):
    __tablename__ = "learning_collections"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    owner_id = Column(BigInteger, ForeignKey("users.id", ondelete="CASCADE"), index=True)
    added_at = Column(DateTime, default=datetime.datetime.utcnow)
    is_public = Column(Boolean, default=False)

    owner = relationship("User", back_populates="owned_learning_collections", foreign_keys=[owner_id])
    cards = relationship("LearningCard", back_populates="learning_collection")
    learning_sessions = relationship("LearningSession", back_populates="learning_collection")
    users = relationship("UserLearningCollection", back_populates="learning_collection")
