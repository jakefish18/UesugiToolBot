"""
There are bot initialization and database package adding.
"""

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from core import settings

# Bot initialization.
bot: Bot = Bot(settings.BOT_TOKEN)
bot_dispatcher: Dispatcher = Dispatcher(bot, storage=MemoryStorage())
