from aiogram import Dispatcher, types
from aiogram.dispatcher.storage import FSMContext

from src.telegram_bot.keyboard_markups import kbm_main_menu

CANCEL_COMMAND_RESPONSE_1 = "✅ Отменено."
CANCEL_COMMAND_RESPONSE_2 = "✅ Нечего отменять."


async def cancel(message: types.Message, state: FSMContext):
    """Cancel command."""
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.reply(CANCEL_COMMAND_RESPONSE_1, reply_markup=kbm_main_menu)
    else:
        await message.reply(CANCEL_COMMAND_RESPONSE_2, reply_markup=kbm_main_menu)


def register_cancel_command(bot_dispatcher: Dispatcher):
    bot_dispatcher.register_message_handler(cancel, commands=["cancel"], state="*")
