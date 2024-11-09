from aiogram import Dispatcher, types

from crud import crud_user
from db import SessionLocal
from models import User
from telegram_bot.init import bot
from telegram_bot.keyboard_markups import kbm_main_menu

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
    if crud_user.get_by_telegram_id(db, user_telegram_id):
        db.close()
        await bot.send_message(user_telegram_id, START_COMMAND_RESPONSE, reply_markup=kbm_main_menu)
        return

    user = User(telegram_id=user_telegram_id)
    user = crud_user.create(db, user)
    await bot.send_message(user.telegram_id, START_COMMAND_RESPONSE, reply_markup=kbm_main_menu)

    db.close()


def register_start_command(bot_dispatcher: Dispatcher):
    bot_dispatcher.register_message_handler(start, commands=["start"])
