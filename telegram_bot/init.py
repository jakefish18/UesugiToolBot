"""
There are bot initialization and database package adding.
"""

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import BOT_TOKEN
import database_handlers

# Database handlers initialization.
users = database_handlers.Users()
user_learning_collections = database_handlers.UserLearningCollections()
learning_collection_items = database_handlers.LearningCollectionItems()
user_learning_sessions = database_handlers.UserLearningSessions()
learning_sessions = database_handlers.LearningSessions()

# Bot initialization.
bot: Bot = Bot(BOT_TOKEN)
bot_dispatcher: Dispatcher = Dispatcher(bot, storage=MemoryStorage())

