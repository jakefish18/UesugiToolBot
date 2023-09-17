from aiogram import Dispatcher, types

from src.crud import crud_user
from src.db import SessionLocal
from src.models import User
from src.telegram_bot.init import bot
from src.telegram_bot.keyboard_markups import kbm_main_menu

LIST_LEARNING_COLLECTION_ERROR_1 = "Ошибка! У вас нет добавленных тренировок!"


async def list_learning_collections(query: types.CallbackQuery):
    """
    Adding user into the database after
    user executes /start command.
    """
    db = SessionLocal()

    user_telegram_id = query.from_user.id
    user = crud_user.get_by_telegram_id(db, user_telegram_id)
    user_learning_collection_names = [
        user_learning_collection.learning_collection.name for user_learning_collection in user.learning_collections
    ]

    response_message = "\n".join(user_learning_collection_names)

    if not response_message:
        response_message = LIST_LEARNING_COLLECTION_ERROR_1

    await bot.send_message(user.telegram_id, response_message, reply_markup=kbm_main_menu)


def register_list_learning_collections_command(bot_dispatcher: Dispatcher):
    bot_dispatcher.register_callback_query_handler(list_learning_collections, text="list_learning_collections")
