import src.models
from src.db import Base, engine

Base.metadata.create_all(bind=engine)

from src.telegram_bot import run_bot

run_bot()
