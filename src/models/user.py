"""User SQLAlchemy model."""
import datetime

from sqlalchemy import BigInteger, Column, DateTime, Integer
from sqlalchemy.orm import relationship

from src.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    telegram_id = Column(BigInteger, unique=True, index=True)
    registered_at = Column(DateTime, default=datetime.datetime.utcnow)

    learning_session = relationship("LearningSession", back_populates="user")
    learning_collections = relationship("LearningCollection", back_populates="owner")
