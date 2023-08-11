from typing import List

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def generate(button_titles: List[List[List]]) -> InlineKeyboardMarkup:
    """
    Inline keyboard creation.
    Generating keyboard markup by inputed layout list.
    Every button must have button title and button callback.

    Exmaple:
    if there is such list
    [
        [["Hello", "start"], ["Information", "info"]],
        [["Add offer", "add_offer"], ["Del offer", "del_offer"]]
    ]
    the result inline keyabord will be with the same layout and callbacks
        Hello       Infomation
        Add offer   Del Offer
    """
    kbm = InlineKeyboardMarkup()

    for row in button_titles:
        keyboard_row_buttons = []

        for button_title, button_callback in row:
            button = InlineKeyboardButton(text=button_title, callback_data=button_callback)
            keyboard_row_buttons.append(button)

        kbm.add(*keyboard_row_buttons)

    return kbm
