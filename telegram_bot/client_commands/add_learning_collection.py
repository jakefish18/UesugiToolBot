import json
from aiogram import types
from aiogram import Dispatcher
from aiogram.dispatcher.storage import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils.callback_data import CallbackData

from telegram_bot.init import bot, users, user_learning_collections, learning_collection_items
from telegram_bot.keyboard_markups import kbm_main_menu


class LearningCollectionForm(StatesGroup):
    name = State()
    file = State()


# Bot responses and errors for this command.
ADD_LEARNING_COLLECTION_RESPONSE_1 = "Чтобы добавить новую коллекцию для тренировки, " \
                                     "отправьте название этой коллекции:"
ADD_LEARNING_COLLECTION_ERROR_1 = "Ошибка! Вы уже добавляли коллекцию для тренировок с таким названием, выберете другое."
ADD_LEARNING_COLLECTION_RESPONSE_2 = "Успешно! Теперь отправьте JSON-файл, где в качестве ключа содержатся ответы, " \
                                     "а ответы являются их значениями:"
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
    user_telegram_id = message.from_user.id
    learning_collection_name = message.text

    user_id = users.get_user_id(user_telegram_id)
    is_added = user_learning_collections.add_user_learning_collection(user_id, learning_collection_name)
    if is_added:
        # Saving data for future steps.
        learning_collection_id = user_learning_collections.get_learning_collection_id(user_id, learning_collection_name)
        async with state.proxy() as learning_collection_info:
            learning_collection_info["user_id"] = user_id
            learning_collection_info["id"] = learning_collection_id
            learning_collection_info["name"] = learning_collection_name
            learning_collection_info.update()

        await LearningCollectionForm.file.set()
        await bot.send_message(
            user_telegram_id,
            ADD_LEARNING_COLLECTION_RESPONSE_2
        )

    else:
        await state.finish()
        await bot.send_message(user_telegram_id, ADD_LEARNING_COLLECTION_ERROR_1, reply_markup=kbm_main_menu)

async def add_learning_collection_st3(message: types.message, state: FSMContext):
    """
    Get the learning collection file from the user.
    """

    # Downloading JSON file.
    user_telegram_id = message.from_user.id
    learning_collection_file_id = message.document.file_id
    learning_collection_file = await bot.get_file(learning_collection_file_id)
    path_to_save_learning_collection_file = f"user_files/{user_telegram_id}.json"
    await bot.download_file(learning_collection_file.file_path, path_to_save_learning_collection_file)
    with open(path_to_save_learning_collection_file, 'r', encoding="UTF-8") as learning_collection_file:
        learning_collection = json.load(learning_collection_file)

    # Getting learning collection id.
    async with state.proxy() as learning_collection_info:
        learning_collection_id = learning_collection_info["id"]

    # Inserting.
    learning_collection_items.add_learning_collection_items(learning_collection_id, learning_collection)

    await state.finish()
    await bot.send_message(user_telegram_id, ADD_LEARNING_COLLECTION_RESPONSE_3)




def register_add_learning_collection_command(bot_dispatcher: Dispatcher):
    bot_dispatcher.register_callback_query_handler(add_learning_collection_st1, text="add_learning_collection")
    bot_dispatcher.register_message_handler(add_learning_collection_st2, state=LearningCollectionForm.name)
    bot_dispatcher.register_message_handler(
        add_learning_collection_st3, content_types=types.ContentType.DOCUMENT, state=LearningCollectionForm.file
    )