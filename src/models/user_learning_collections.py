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
    UniqueConstraint
)
from sqlalchemy.orm import relationship

from db import Base


class UserLearningCollection(Base):
    __tablename__ = "user_learning_collections"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    learning_collection_id = Column(Integer, ForeignKey("learning_collections.id", ondelete="CASCADE"))

    user = relationship("User", back_populates="learning_collections", uselist=False, foreign_keys=[user_id])
    learning_collection = relationship(
        "LearningCollection", back_populates="users", uselist=False, foreign_keys=[learning_collection_id]
    )

    __table_args__ = (
        UniqueConstraint("user_id", "learning_collection_id", name="_user_id_learning_collection_id_uc"),
    )