"""
Importing all bot functions from files and bot launching.
"""

from aiogram import Dispatcher
from aiogram.utils import executor

from src.telegram_bot.client_commands import (
    register_add_learning_collection_command,
    register_cancel_command,
    register_del_learning_collection_command,
    register_get_auth_token_command,
    register_info_command,
    register_list_learning_collections_command,
    register_menu_command,
    register_publish_learning_collection_command,
    register_run_learning_session_command,
    register_search_learning_collection_command,
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
    register_info_command(bot_dispatcher)
    register_list_learning_collections_command(bot_dispatcher)
    register_menu_command(bot_dispatcher)
    register_publish_learning_collection_command(bot_dispatcher)
    register_search_learning_collection_command(bot_dispatcher)
    register_get_auth_token_command(bot_dispatcher)


def run_bot():
    executor.start_polling(dispatcher=bot_dispatcher, skip_updates=True, on_startup=on_startup)


if __name__ == "__main__":
    run_bot()
