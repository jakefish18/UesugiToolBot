import random

from aiogram import Dispatcher, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.storage import FSMContext
from aiogram.utils.callback_data import CallbackData

from src.crud import (
    crud_learning_collection,
    crud_learning_session,
    crud_learning_session_card,
    crud_user,
)
from src.db import SessionLocal
from src.models import LearningSession, LearningSessionCard, User
from src.telegram_bot.init import bot
from src.telegram_bot.keyboard_markups import kbm_main_menu, reply_kbm


class LearningSessionForm(StatesGroup):
    name = State()
    session = State()


RUN_LEARNING_SESSION_ERROR_1 = "Ошибка! У вас ещё нет добавленных тренировок."
RUN_LEARNING_SESSION_RESPONSE_1 = "Чтобы начать тренировку, выберите её:"
RUN_LEARNING_SESSION_ERROR_2 = "Ошибка! У вас нет такой тренировки."
RUN_LEARNING_SESSION_ERROR_3 = "Неправильный ответ :("
RUN_LEARNING_SESSION_RESPONSE_3 = "Успешно. Вы прошли всю тренировку!!! :)"


# Supporting functions.
def list_transformation(x: str) -> list[str]:
    """Returning list with single object x."""
    return [x]


# Command functions.
async def run_learning_session_st1(message: types.message):
    """
    Run learning session.
    Send keyboard with choose to user.
    """
    db = SessionLocal()
    user_telegram_id = message.from_user.id
    user: User = crud_user.get_by_telegram_id(db, user_telegram_id)

    # Creating reply keyboard with user learning collections.
    learning_collection_names: list[str] = [
        learning_collection.name for learning_collection in user.learning_collections
    ]

    # Error if user hasn't added learning collections.
    if len(learning_collection_names) == 0:
        await bot.send_message(user_telegram_id, RUN_LEARNING_SESSION_ERROR_1, reply_markup=kbm_main_menu)
        return

    learning_collection_names_layout = list(map(list_transformation, learning_collection_names))
    kbm_learning_collection_names = reply_kbm.generate(learning_collection_names_layout)

    await LearningSessionForm.name.set()
    await bot.send_message(
        user_telegram_id, RUN_LEARNING_SESSION_RESPONSE_1, reply_markup=kbm_learning_collection_names
    )

    db.close()


async def run_learning_session_st2(message: types.message, state: FSMContext):
    """
    Get user learning collection name for learning session,
    launching learning session and adding to user learning sessions table.
    """
    db = SessionLocal()

    user_telegram_id = message.from_user.id
    learning_collection_name = message.text

    user = crud_user.get_by_telegram_id(db, user_telegram_id)
    learning_collection = crud_learning_collection.get_by_name(db, user, learning_collection_name)

    # Error if user has entered unknown learning collection.
    if not learning_collection:
        await state.finish()
        await bot.send_message(user_telegram_id, RUN_LEARNING_SESSION_ERROR_2, reply_markup=kbm_main_menu)
        return

    # Deleting past sessions if it exists.
    past_learning_session = crud_learning_session.get_user_session(db, user)

    if past_learning_session:
        crud_learning_session.delete(db, past_learning_session.id)

    # Setting up learning session.
    learning_session = LearningSession(user_id=user.id, learning_collection_id=learning_collection.id)
    learning_session = crud_learning_session.create(db, learning_session)
    user = crud_user.set_learning_session(db, user, learning_session)
    learning_collection_card_ids = [card.id for card in learning_collection.cards]
    crud_learning_session.create(db, learning_session)

    learning_session_cards: list[LearningSessionCard] = []
    for card_id in learning_collection_card_ids:
        learning_session_card = LearningSessionCard(learning_session_id=learning_session.id, card_id=card_id)
        learning_session_cards.append(learning_session_card)

    crud_learning_session.create_many(db, learning_session_cards)

    # Preparing data for learning session.
    async with state.proxy() as answer:
        answer["answered_count"] = 0
        answer["choosen_training"] = learning_collection.name
        answer["total_count_of_cards"] = len(learning_collection.cards)

    db.close()

    await continue_learning_session(message, state, first_question=True)


async def continue_learning_session(message: types.message, state: FSMContext, first_question=False):
    """Sending questions before user fails."""
    db = SessionLocal()

    user_telegram_id = message.from_user.id
    user = crud_user.get_by_telegram_id(db, user_telegram_id)

    # Checking past answer.
    if not first_question:
        async with state.proxy() as answer:
            if answer["answer"] != message.text:
                await state.finish()
                answered_count = answer["answered_count"]
                total_count_of_cards = answer["total_count_of_cards"]
                await bot.send_message(
                    user_telegram_id,
                    f"Сделано: {answered_count}/{total_count_of_cards}\n"
                    + f'Вопрос: {answer["question"]}\n'
                    + f'Правильный ответ: {answer["answer"]}\n'
                    + f"Ваш ответ: {message.text}\n"
                    + RUN_LEARNING_SESSION_ERROR_3,
                    reply_markup=kbm_main_menu,
                )
                return

            answer_card_id = answer["answer_card_id"]

            # Setting past answer to passed.
            passed_card = crud_learning_session_card.get(db, answer_card_id)
            passed_card.is_passed = True
            passed_card = crud_learning_session_card.update(db, passed_card)

            # Saving answered count for session.
            answer["answered_count"] += 1

    # Get user learning session.
    learning_session = crud_learning_session.get_user_session(db, user)

    # Get question.
    answer_card = crud_learning_session_card.get_answer_card(db, learning_session)

    if not answer_card:
        await state.finish()
        await bot.send_message(user_telegram_id, RUN_LEARNING_SESSION_RESPONSE_3, reply_markup=kbm_main_menu)
        return

    other_cards = crud_learning_session_card.get_extra_cards(db, answer_card, learning_session, 3)

    card_question = answer_card.card.question

    # Saving answer.
    async with state.proxy() as answer:
        answer["answer_card_id"] = answer_card.id
        answer["question"] = answer_card.card.question
        answer["answer"] = answer_card.card.answer
        answer.update()

    # Answer option must contain list of lists to generate keyboard correctly.
    answer_options = [[answer_card.card.answer]]

    for other_card in other_cards:
        answer_options.append([other_card.card.answer])

    random.shuffle(answer_options)

    kbm_answers = reply_kbm.generate(answer_options)

    await bot.send_message(user_telegram_id, card_question, reply_markup=kbm_answers)
    await LearningSessionForm.session.set()

    db.close()


# Command registration function.
def register_run_learning_session_command(bot_dispatcher: Dispatcher):
    bot_dispatcher.register_callback_query_handler(run_learning_session_st1, text="run_learning_session")
    bot_dispatcher.register_message_handler(run_learning_session_st2, state=LearningSessionForm.name)
    bot_dispatcher.register_message_handler(continue_learning_session, state=LearningSessionForm.session)
