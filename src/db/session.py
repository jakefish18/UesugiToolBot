"""
Creating database engine and such things.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from core import settings

engine = create_engine(settings.DATABASE_URI, pool_size=300, max_overflow=500, pool_timeout=600, pool_recycle=1800, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
