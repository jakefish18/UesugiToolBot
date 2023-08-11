import json

from aiogram import Dispatcher, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.storage import FSMContext

from src.crud import crud_learning_card, crud_learning_collection, crud_user
from src.db import SessionLocal
from src.models import LearningCard, LearningCollection, User
from src.telegram_bot.init import bot
from src.telegram_bot.keyboard_markups import kbm_main_menu


class LearningCollectionForm(StatesGroup):
    name = State()
    file = State()


# Bot responses and errors for this command.
ADD_LEARNING_COLLECTION_RESPONSE_1 = (
    "Чтобы добавить новую коллекцию для тренировки, " "отправьте название этой коллекции:"
)
ADD_LEARNING_COLLECTION_ERROR_1 = (
    "Ошибка! Вы уже добавляли коллекцию для тренировок с таким названием, выберете другое."
)
ADD_LEARNING_COLLECTION_RESPONSE_2 = (
    "Успешно! Теперь отправьте JSON-файл, где в качестве ключа содержатся ответы, " "а ответы являются их значениями:"
)
ADD_LEARNING_COLLECTION_ERROR_2 = "Ошибка! Файл повреждён или не соответствует требованиям."
ADD_LEARNING_COLLECTION_RESPONSE_3 = "Успешно! Тренировка добавлена."


async def add_learning_collection_st1(query: types.CallbackQuery):
    """
    Launching add learning collection command.
    Firstly requests collection name.
    """
    user_telegram_id = query.from_user.id
    await LearningCollectionForm.name.set()
    await bot.send_message(user_telegram_id, ADD_LEARNING_COLLECTION_RESPONSE_1)


async def add_learning_collection_st2(message: types.message, state: FSMContext):
    """
    Get the learning collection name from the user.
    Then asking for a JSON file with training collection.
    """
    db = SessionLocal()

    user_telegram_id = message.from_user.id
    learning_collection_name = message.text

    user = crud_user.get_by_telegram_id(db, user_telegram_id)

    if not user:  # Creating user if user doesn't exist.
        user = User(telegram_id=user_telegram_id)
        user = crud_user.create(db, user)

    is_learning_collection_name_used = crud_learning_collection.get_by_name(db, user, learning_collection_name)
    if not is_learning_collection_name_used:
        # Saving data for future steps.
        learning_collection = LearningCollection(name=learning_collection_name, owner_id=user.id)
        learning_collection = crud_learning_collection.create(db, learning_collection)
        async with state.proxy() as learning_collection_info:
            learning_collection_info["owner_id"] = user.id
            learning_collection_info["id"] = learning_collection.id
            learning_collection_info["name"] = learning_collection.name
            learning_collection_info.update()

        await LearningCollectionForm.file.set()
        await bot.send_message(user_telegram_id, ADD_LEARNING_COLLECTION_RESPONSE_2)

    else:
        await state.finish()
        await bot.send_message(user_telegram_id, ADD_LEARNING_COLLECTION_ERROR_1, reply_markup=kbm_main_menu)

    db.close()


async def add_learning_collection_st3(message: types.message, state: FSMContext):
    """
    Get the learning collection file from the user.
    """
    db = SessionLocal()

    # Downloading JSON file.
    user_telegram_id = message.from_user.id
    learning_collection_file_id = message.document.file_id
    learning_collection_file = await bot.get_file(learning_collection_file_id)
    path_to_save_learning_collection_file = f"user_files/{user_telegram_id}.json"
    await bot.download_file(learning_collection_file.file_path, path_to_save_learning_collection_file)
    with open(path_to_save_learning_collection_file, "r", encoding="UTF-8") as learning_collection_file:
        learning_collection = json.load(learning_collection_file)

    # Getting learning collection id.
    async with state.proxy() as learning_collection_info:
        learning_collection_id = learning_collection_info["id"]

    # Inserting.
    learning_collection_cards: list[LearningCard] = []
    for learning_card_question, learning_card_answer in learning_collection.items():
        learning_card = LearningCard(
            learning_collection_id=learning_collection_id, question=learning_card_question, answer=learning_card_answer
        )
        learning_collection_cards.append(learning_card)

    crud_learning_card.create_many(db, learning_collection_cards)

    await state.finish()
    await bot.send_message(user_telegram_id, ADD_LEARNING_COLLECTION_RESPONSE_3)

    db.close()


def register_add_learning_collection_command(bot_dispatcher: Dispatcher):
    bot_dispatcher.register_callback_query_handler(add_learning_collection_st1, text="add_learning_collection")
    bot_dispatcher.register_message_handler(add_learning_collection_st2, state=LearningCollectionForm.name)
    bot_dispatcher.register_message_handler(
        add_learning_collection_st3, content_types=types.ContentType.DOCUMENT, state=LearningCollectionForm.file
    )
