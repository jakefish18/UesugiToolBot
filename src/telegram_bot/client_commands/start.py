from aiogram import Dispatcher, types

from src.crud import crud_user
from src.db import SessionLocal
from src.models import User
from src.telegram_bot.init import bot
from src.telegram_bot.keyboard_markups import kbm_main_menu

START_COMMAND_RESPONSE = (
    "✅ Вы были успешно зарегестрированы! Чтобы узнать, как пользоваться ботом" 'нажмите на кнопку "Информация" в меню.'
)


async def start(message: types.message):
    """
    Adding user into the database after
    user executes /start command.
    """
    db = SessionLocal()

    user_telegram_id = message.from_user.id
    user = User(telegram_id=user_telegram_id)
    user = crud_user.create(db, user)
    await bot.send_message(user.telegram_id, START_COMMAND_RESPONSE, reply_markup=kbm_main_menu)

    db.close()


def register_start_command(bot_dispatcher: Dispatcher):
    bot_dispatcher.register_message_handler(start, commands=["start"])
