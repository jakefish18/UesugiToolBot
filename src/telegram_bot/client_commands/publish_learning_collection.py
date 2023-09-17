from aiogram import Dispatcher, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.storage import FSMContext

from src.crud import crud_learning_collection, crud_user
from src.db import SessionLocal
from src.telegram_bot.init import bot
from src.telegram_bot.keyboard_markups import (
    kbm_learning_collections,
    kbm_main_menu,
    kbm_y_or_n,
)


class PublishCollectionForm(StatesGroup):
    name = State()
    y_or_n = State()


PUBLISH_LEARNING_COLLECTION_ERROR_1 = 'Ошибка! У вас ещё нет добавленных тренировок. Чтобы узнать, как добавлять тренировки, нажмите на кнопку "Информация"'
PUBLISH_LEARNING_COLLECTION_RESPONSE_1 = "Выберите из списка тренировку, которую хотите опубликовать:"
PUBLISH_LEARNING_COLLECTION_ERROR_2 = "Ошибка! У ваc нет тренировки под таким названием."
PUBLISH_LEARNING_COLLECTION_RESPONSE_2 = "Вы действительно хотите опубликовать тренировку?"
PUBLISH_LEARNING_COLLECTION_RESPONSE_3_1 = "Отменено!"
PUBLISH_LEARNING_COLLECTION_RESPONSE_3_2 = (
    "✅Успешно! Ваша тренировка опубликована. Другие пользователи могут найти её, введя ваш ник и название тренировки."
)


async def publish_learning_collection_st1(query: types.CallbackQuery):
    """
    Command to publish learning collection.
    Firtsly request the name of learning collection to publish.
    """
    db = SessionLocal()

    user_telegram_id = query.from_user.id
    user = crud_user.get_by_telegram_id(db, user_telegram_id)

    # Error if user hasn't added learning collections.
    if len(user.learning_collections) == 0:
        await bot.send_message(user_telegram_id, PUBLISH_LEARNING_COLLECTION_ERROR_1, reply_markup=kbm_main_menu)
        return

    kbm_learning_collection_names = kbm_learning_collections.generate(user)

    await PublishCollectionForm.name.set()
    await bot.send_message(
        user_telegram_id, PUBLISH_LEARNING_COLLECTION_RESPONSE_1, reply_markup=kbm_learning_collection_names
    )

    db.close()


async def publish_learning_collection_st2(message: types.message, state: FSMContext):
    """
    Getting the name of learning collection to publish and passing into next stage.
    Sending the yes_or_no keyboard markup.
    """
    db = SessionLocal()

    user_telegram_id = message.from_user.id
    user = crud_user.get_by_telegram_id(db, user_telegram_id)
    learning_collection_name = message.text

    learning_collection = crud_learning_collection.get_by_name(db, user, learning_collection_name)

    if not learning_collection:
        await state.finish()
        await bot.send_message(user.telegram_id, PUBLISH_LEARNING_COLLECTION_ERROR_2, reply_markup=kbm_main_menu)
        return

    async with state.proxy() as learning_collection_data:
        learning_collection_data["name"] = learning_collection_name

    await PublishCollectionForm.y_or_n.set()
    await bot.send_message(user.telegram_id, PUBLISH_LEARNING_COLLECTION_RESPONSE_2, reply_markup=kbm_y_or_n)

    db.close()


async def public_learning_collection_st3(query: types.CallbackQuery, state: FSMContext):
    """
    Getting the answer to yes or no question.
    Publishing the learning collection if the use answered yes.
    """
    db = SessionLocal()

    user_telegram_id = query.from_user.id
    user = crud_user.get_by_telegram_id(db, user_telegram_id)

    if query.data == "no":
        await state.finish()
        await bot.send_message(user.telegram_id, PUBLISH_LEARNING_COLLECTION_RESPONSE_3_1, reply_markup=kbm_main_menu)
        return

    async with state.proxy() as learning_collection_data:
        learning_collection_name = learning_collection_data["name"]
        learning_collection = crud_learning_collection.get_by_name(db, user, learning_collection_name)
        learning_collection = crud_learning_collection.update_to_public(db, learning_collection)

    await state.finish()
    await bot.send_message(user.telegram_id, PUBLISH_LEARNING_COLLECTION_RESPONSE_3_2, reply_markup=kbm_main_menu)
    db.close()


def register_publish_learning_collection_command(bot_dispatcher: Dispatcher):
    bot_dispatcher.register_callback_query_handler(publish_learning_collection_st1, text="publish_learning_collection")
    bot_dispatcher.register_message_handler(publish_learning_collection_st2, state=PublishCollectionForm.name)
    bot_dispatcher.register_callback_query_handler(
        public_learning_collection_st3,
        lambda callback_query: callback_query.data in ("yes", "no"),
        state=PublishCollectionForm.y_or_n,
    )
