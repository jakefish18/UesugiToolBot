from aiogram import Dispatcher, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.storage import FSMContext

import cache_db
from core import security
from crud import crud_auth_token, crud_user
from db import SessionLocal
from telegram_bot.init import bot
from telegram_bot.keyboard_markups import kbm_main_menu


class Form(StatesGroup):
    state = State()


RESPONSE_1 = ""


async def get_auth_token(query: types.CallbackQuery):
    """Sending acces to the utbothelper."""
    db = SessionLocal()
    redis = cache_db.open()

    user_telegram_id = query.from_user.id
    user = crud_user.get_by_telegram_id(db, user_telegram_id)

    token = security.create_token()
    auth_token = crud_auth_token.create(redis, user, token)

    await bot.send_message(
        user.telegram_id,
        f"Ваш доступ: http://127.0.0.1:8000/auth/login?auth-token={auth_token}",
        reply_markup=kbm_main_menu,
    )

    redis.close()
    db.close()


def register_get_auth_token_command(bot_dispatcher: Dispatcher):
    bot_dispatcher.register_callback_query_handler(get_auth_token, text="get_auth_token")
