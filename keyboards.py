from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def create_keyboard(*buttons):
    markup = ReplyKeyboardMarkup
    for button in buttons:
        markup.add(ReplyKeyboardMarkup(button))
    return markup
