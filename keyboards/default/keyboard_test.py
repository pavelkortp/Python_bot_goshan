from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import KeyboardButton
kb_test = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text ='/menu')
        ],

    ],
    resize_keyboard=True
)