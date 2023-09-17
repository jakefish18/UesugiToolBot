from src.telegram_bot.keyboard_markups import inline_kbm

main_menu_layout = [
    [["ℹ️Информация", "info"], ["🧠 Запустить тренировку", "run_learning_session"]],
    [["📝Добавить тренировку", "add_learning_collection"], ["🗑Удалить тренировку", "del_learning_collection"]],
    [
        ["🗂Вывести список тренировок", "list_learning_collections"],
        ["🌐Опубликовать тренировку", "publish_learning_collection"],
    ],
    [["Искать тренировку", "search_learning_collection"]],
]
kbm_main_menu = inline_kbm.generate(main_menu_layout)
