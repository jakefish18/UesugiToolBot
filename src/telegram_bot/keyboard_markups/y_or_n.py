from src.telegram_bot.keyboard_markups import inline_kbm

y_or_n_layout = [[["✅Да", "yes"], ["❌Нет", "no"]]]
kbm_y_or_n = inline_kbm.generate(y_or_n_layout)
