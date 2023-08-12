import json

from aiogram import Dispatcher, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.storage import FSMContext

from src.crud import crud_learning_card, crud_learning_collection, crud_user
from src.db import SessionLocal
from src.models import LearningCard, LearningCollection, User
from src.telegram_bot.init import bot
from src.telegram_bot.keyboard_markups import kbm_main_menu, reply_kbm


class DelCollectionForm(StatesGroup):
    name = State()


DEL_LEARNING_COLLECTION_ERROR_1 = "Ошибка! У вас ещё нет добавленных тренировок."
DEL_LEARNING_COLLECTION_RESPONSE_1 = "Выберите из списка тренировку, которую хотите удалить:"
DEL_LEARNING_COLLECTION_ERROR_2 = "Ошибка! У ваc нет тренировки под таким названием."
DEL_LEARNING_COLLECTION_RESPONSE_2 = "✅ Успешно! Удалено."


# Supporting functions.
def list_transformation(x: str) -> list[str]:
    """Returning list with single object x."""
    return [x]


async def del_learning_collection_st1(query: types.CallbackQuery):
    """
    Delete learning collection command.
    Firstly requesting collection name for delete.
    """
    db = SessionLocal()

    user_telegram_id = query.from_user.id
    user = crud_user.get_by_telegram_id(db, user_telegram_id)

    # Creating reply keyboard with user learning collections.
    learning_collection_names: list[str] = [
        learning_collection.name for learning_collection in user.learning_collections
    ]

    # Error if user hasn't added learning collections.
    if len(learning_collection_names) == 0:
        await bot.send_message(user_telegram_id, DEL_LEARNING_COLLECTION_ERROR_1, reply_markup=kbm_main_menu)
        return

    learning_collection_names_layout = list(map(list_transformation, learning_collection_names))
    kbm_learning_collection_names = reply_kbm.generate(learning_collection_names_layout)

    await DelCollectionForm.name.set()
    await bot.send_message(
        user_telegram_id, DEL_LEARNING_COLLECTION_RESPONSE_1, reply_markup=kbm_learning_collection_names
    )

    db.close()


async def del_learning_collection_st2(message: types.message, state: FSMContext):
    """
    Deleting entered learning collection from db.
    """
    db = SessionLocal()

    user_telegram_id = message.from_user.id
    user = crud_user.get_by_telegram_id(db, user_telegram_id)
    learning_collection_name = message.text

    learning_collection = crud_learning_collection.get_by_name(db, user, learning_collection_name)

    if not learning_collection:
        await state.finish()
        await bot.send_message(user.telegram_id, DEL_LEARNING_COLLECTION_ERROR_2, reply_markup=kbm_main_menu)
        return

    crud_learning_collection.delete(db, learning_collection.id)

    await state.finish()
    await bot.send_message(user.telegram_id, DEL_LEARNING_COLLECTION_RESPONSE_2, reply_markup=kbm_main_menu)

    db.close()


def register_del_learning_collection_command(bot_dispatcher: Dispatcher):
    bot_dispatcher.register_callback_query_handler(del_learning_collection_st1, text="del_learning_collection")
    bot_dispatcher.register_message_handler(del_learning_collection_st2, state=DelCollectionForm.name)
