import aiogram.utils.markdown as fmt
from aiogram import Dispatcher, types

from src.telegram_bot.init import bot
from src.telegram_bot.keyboard_markups import kbm_main_menu

INFO_RESPONSE_1 = fmt.text(
    fmt.text("👋 " + fmt.hbold("Приветствую") + "!"),
    fmt.text(
        "❓ Этот бот предназначен для заучивания",
        fmt.hbold('"карт"') + ".",
        "Под",
        fmt.hbold('"картой"'),
        "подразумевается пара вопрос-ответ.",
        sep=" ",
    ),
    fmt.text(
        "🤔 Пример: у меня есть список из 300 английских слов, которые мне надо выучить. Для того, чтобы учить было приятнее, интереснее, а также иметь доступ в любом месте, я использую этого бота:"
    ),
    fmt.text(
        "📄 1. Первым делом я загружаю",
        fmt.hcode("learning_collection.json"),
        "файл функцией",
        fmt.hbold('"Добавить тренировку,"'),
        "где ключ — слово на английском, а значение — перевод на русский.",
        sep=" ",
    ),
    fmt.text(
        "🏃 2. Дальше я запускаю эту тренировку функцией",
        fmt.hbold('"Запустить тренировку"'),
        ", и мне будут присылаться вопросы с вариантами ответом.",
        sep=" ",
    ),
    fmt.text("🎯 3. А сама тренировка закончится, когда вы ошибетесь или пройдёте всё, что есть."),
    fmt.text("❌ Тренировку можно завершить досрочно, отправив команду", fmt.hcode("/cancel") + ".", sep=" "),
    fmt.text("📱 Меню команд можно вызвать, отправив команду", fmt.hcode("/menu") + ".", sep=" "),
    fmt.text("🍀", fmt.hbold("Удачи!"), sep=" "),
    sep="\n\n",
)


async def info(query: types.CallbackQuery):
    """
    Sending info about bot.
    """
    user_telegram_id = query.from_user.id
    await bot.send_message(
        user_telegram_id, INFO_RESPONSE_1, reply_markup=kbm_main_menu, parse_mode=types.ParseMode.HTML
    )


def register_info_command(bot_dispatcher: Dispatcher):
    bot_dispatcher.register_callback_query_handler(info, text="info")
