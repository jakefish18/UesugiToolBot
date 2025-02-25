import json

from aiogram import Dispatcher, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.storage import FSMContext

from crud import crud_learning_card, crud_learning_collection, crud_user
from db import SessionLocal
from models import LearningCard, LearningCollection, User
from telegram_bot.init import bot
from telegram_bot.keyboard_markups import kbm_learning_collections, kbm_main_menu


class DelCollectionForm(StatesGroup):
    name = State()


DEL_LEARNING_COLLECTION_ERROR_1 = 'Ошибка! У вас ещё нет добавленных тренировок. Чтобы узнать, как добавлять тренировки, нажмите на кнопку "Информация"'
DEL_LEARNING_COLLECTION_RESPONSE_1 = "Выберите из списка тренировку, которую хотите удалить:"
DEL_LEARNING_COLLECTION_ERROR_2 = "Ошибка! У ваc нет тренировки под таким названием."
DEL_LEARNING_COLLECTION_RESPONSE_2 = "✅ Успешно! Удалено."


async def del_learning_collection_st1(query: types.CallbackQuery):
    """
    Delete learning collection command.
    Firstly requesting collection name for delete.
    """
    db = SessionLocal()

    user_telegram_id = query.from_user.id
    user = crud_user.get_by_telegram_id(db, user_telegram_id)

    # Error if user hasn't added learning collections.
    if len(user.learning_collections) == 0:
        await bot.send_message(user_telegram_id, DEL_LEARNING_COLLECTION_ERROR_1, reply_markup=kbm_main_menu)
        return

    kbm_learning_collection_names = kbm_learning_collections.generate(user)

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
