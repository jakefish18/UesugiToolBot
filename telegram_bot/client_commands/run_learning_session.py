import random
from typing import List
from aiogram import types
from aiogram import Dispatcher
from aiogram.dispatcher.storage import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils.callback_data import CallbackData

from telegram_bot.init import (
    bot,
    users, user_learning_collections, user_learning_sessions, learning_sessions, learning_collection_items
)
from telegram_bot.keyboard_markups import kbm_main_menu
from telegram_bot.keyboard_markups import reply_kbm


class LearningSessionForm(StatesGroup):
    name = State()
    sessions = State()


RUN_LEARNING_SESSION_ERROR_1 = "Ошибка! У вас ещё нет добавленных тренировок."
RUN_LEARNING_SESSION_RESPONSE_1 = "Чтобы начать тренировку, выберите её:"
RUN_LEARNING_SESSION_ERROR_2 = "Ошибка! У вас нет такой тренировки."

# Supporting functions.
def list_transformation(x: str) -> List:
    """Returning list with single object x."""
    return [x]

# Command functions.
async def run_learning_session_st1(message: types.message):
    """
    Run learning session.
    Send keyboard with choose to user.
    """
    user_telegram_id = message.from_user.id
    user_id = users.get_user_id(user_telegram_id)

    # Creating reply keyboard with user learning collections.
    user_learning_collection_names: List[str] = user_learning_collections.get_user_learning_collection_names(user_id)

    # Error if user hasn't added learning collections.
    if len(user_learning_collection_names) == 0:
        await bot.send_message(user_telegram_id, RUN_LEARNING_SESSION_ERROR_1, reply_markup=kbm_main_menu)
        return

    user_learning_collection_names_layout = list(map(list_transformation, user_learning_collection_names))
    kbm_user_learning_collection_names = reply_kbm.generate(user_learning_collection_names_layout)

    await LearningSessionForm.name.set()
    await bot.send_message(user_telegram_id, RUN_LEARNING_SESSION_RESPONSE_1, reply_markup=kbm_user_learning_collection_names)

async def run_learning_session_st2(message: types.message, state: FSMContext):
    """
    Get user learning collection name for learning session,
    launching learning session and adding to user learning sessions table.
    """
    user_telegram_id = message.from_user.id
    learning_collection_name = message.text

    user_id = users.get_user_id(user_telegram_id)
    learning_collection_id = user_learning_collections.get_learning_collection_id(user_id, learning_collection_name)

    # Error if user has entered unknown learning collection.
    if learning_collection_id == 0:
        await state.finish()
        await bot.send_message(user_telegram_id, RUN_LEARNING_SESSION_ERROR_2, reply_markup=kbm_main_menu)
        return

    # Setting up learning session.
    user_learning_session_id = user_learning_sessions.create_user_learning_session(user_id, learning_collection_id)
    users.set_user_learning_session(user_id, user_learning_session_id)
    learning_collection_card_ids = learning_collection_items.get_learning_collection_card_ids(learning_collection_id)
    learning_sessions.add_learning_session(user_learning_session_id, learning_collection_card_ids)

    # Get first question.
    answer_card_id, other_card_ids = learning_sessions.get_random_cards(user_learning_session_id, 4)
    answer_card = learning_collection_items.get_card_question_and_answer(answer_card_id)

    card_question = answer_card[0]

    # Answer option must contain list of lists to generate keyboard correctly.
    answer_options = [[answer_card[1]]]

    for other_card_id in other_card_ids:
        other_card = learning_collection_items.get_card_question_and_answer(other_card_id)
        answer_options.append([other_card[1]])

    random.shuffle(answer_options)

    kbm_answers = reply_kbm.generate(answer_options)

    await LearningSessionForm.sessions.set()
    await bot.send_message(user_telegram_id, card_question, reply_markup=kbm_answers)

# Command registration function.
def register_run_learning_session_command(bot_dispatcher: Dispatcher):
    bot_dispatcher.register_callback_query_handler(run_learning_session_st1, text="run_learning_session")
    bot_dispatcher.register_message_handler(run_learning_session_st2, state=LearningSessionForm.name)