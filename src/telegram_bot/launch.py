"""
Importing all bot functions from files and bot launching.
"""

from aiogram import Dispatcher
from aiogram.utils import executor

from src.telegram_bot.client_commands import (
    register_add_learning_collection_command,
    register_cancel_command,
    register_del_learning_collection_command,
    register_run_learning_session_command,
    register_start_command,
)
from src.telegram_bot.init import bot_dispatcher


async def on_startup(bot_dispatcher: Dispatcher):
    """
    Registering every command before start.
    """
    register_cancel_command(bot_dispatcher)
    register_start_command(bot_dispatcher)
    register_add_learning_collection_command(bot_dispatcher)
    register_run_learning_session_command(bot_dispatcher)
    register_del_learning_collection_command(bot_dispatcher)


def run_bot():
    executor.start_polling(dispatcher=bot_dispatcher, skip_updates=True, on_startup=on_startup)


if __name__ == "__main__":
    run_bot()
