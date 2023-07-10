"""
Importing all bot functions from files and bot launching.
"""

from aiogram import Dispatcher
from aiogram.utils import executor

from telegram_bot.init import bot_dispatcher
from telegram_bot.client_commands import (
    register_start_command, register_add_learning_collection_command, register_run_learning_session_command
)

async def on_startup(bot_dispatcher: Dispatcher):
    """
    Registering every command before start.
    """
    register_start_command(bot_dispatcher)
    register_add_learning_collection_command(bot_dispatcher)
    register_run_learning_session_command(bot_dispatcher)


def run_bot():
    executor.start_polling(
        dispatcher=bot_dispatcher,
        skip_updates=True,
        on_startup=on_startup
    )


if __name__ == "__main__":
    run_bot()