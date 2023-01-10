from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import KeyboardButton
kb_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text ='10'),
            KeyboardButton(text ='11'),
        ],
        [
            KeyboardButton(text ='/mailing'),
        ],
        [
            KeyboardButton(text ='Інлайн меню'),
            KeyboardButton(text ='Будь-що'),
            KeyboardButton(text ='Like')
        ]
    ],
    resize_keyboard=True
)