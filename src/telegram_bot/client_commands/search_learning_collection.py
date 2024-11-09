from aiogram import Dispatcher, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.storage import FSMContext

from crud import crud_learning_collection, crud_user, crud_user_learning_collection
from db import SessionLocal
from models import UserLearningCollection
from telegram_bot.init import bot
from telegram_bot.keyboard_markups import kbm_main_menu


class SearchCollectionForm(StatesGroup):
    name = State()
    author = State()


SEARCH_LEARNING_COLLECTION_RESPONSE_1 = "Сначала введите название тренировки, которую вы ищете:"
SEARCH_LEARNING_COLLECTION_RESPONSE_2 = "Теперь введите имя автора, от которого эта тренировка:"
SEARCH_LEARNING_COLLECTION_ERROR_3 = "Ошибка! Такая тренировка не найдена."
SEARCH_LEARNING_COLLECTION_RESPONSE_3 = "✅Успешно! Тренировка добавлена."


async def search_learning_collection_st1(query: types.CallbackQuery):
    """Firstly requesting the name of learning collection to search."""
    user_telegram_id = query.from_user.id

    await SearchCollectionForm.name.set()
    await bot.send_message(user_telegram_id, SEARCH_LEARNING_COLLECTION_RESPONSE_1)


async def search_learning_collection_st2(message: types.Message, state: FSMContext):
    """Requesting the author nickanme after the name of learning collection."""
    user_telegram_id = message.from_user.id

    async with state.proxy() as learning_collection_search_data:
        learning_collection_search_data["name"] = message.text

    await bot.send_message(user_telegram_id, SEARCH_LEARNING_COLLECTION_RESPONSE_2)
    await SearchCollectionForm.author.set()


async def search_learning_collection_st3(message: types.Message, state: FSMContext):
    """Searching the learning collection data by the give data. Adding to the user if it is exists."""
    db = SessionLocal()

    user_telegram_id = message.from_user.id
    user = crud_user.get_by_telegram_id(db, user_telegram_id)

    async with state.proxy() as learning_collection_search_data:
        # Getting data from previous stages.
        learning_collection_name = learning_collection_search_data["name"]
        learning_collection_author = message.text

        # Adding learning collection to user.
        finded_learning_collection = crud_learning_collection.get_by_name_and_author_id(
            db, learning_collection_name, learning_collection_author
        )
        # Searching such learning collection.
        if not finded_learning_collection:
            await state.finish()
            await bot.send_message(user_telegram_id, SEARCH_LEARNING_COLLECTION_ERROR_3, reply_markup=kbm_main_menu)
            db.close()
            return

        new_user_learning_collection = UserLearningCollection(
            user_id=user.id, learning_collection_id=finded_learning_collection.id
        )
        crud_user_learning_collection.create(db, new_user_learning_collection)

    await state.finish()
    await bot.send_message(user.telegram_id, SEARCH_LEARNING_COLLECTION_RESPONSE_3, reply_markup=kbm_main_menu)


def register_search_learning_collection_command(bot_dispatcher: Dispatcher):
    bot_dispatcher.register_callback_query_handler(search_learning_collection_st1, text="search_learning_collection")
    bot_dispatcher.register_message_handler(search_learning_collection_st2, state=SearchCollectionForm.name)
    bot_dispatcher.register_message_handler(search_learning_collection_st3, state=SearchCollectionForm.author)
