from aiogram import Dispatcher, types

from src.telegram_bot.init import bot
from src.telegram_bot.keyboard_markups import kbm_main_menu

MENU_REPONSE_1 = "Меню"


async def menu(message: types.Message):
    """
    Sending menu about bot.
    """
    user_telegram_id = message.from_user.id
    await bot.send_message(
        user_telegram_id, MENU_REPONSE_1, reply_markup=kbm_main_menu, parse_mode=types.ParseMode.HTML
    )


def register_menu_command(bot_dispatcher: Dispatcher):
    bot_dispatcher.register_message_handler(menu, commands=["menu"])
