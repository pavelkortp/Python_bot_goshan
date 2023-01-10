from ast import In
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_menu = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Повідомлення', callback_data='Повідомлення'),
                                        InlineKeyboardButton(text='Посилання', url = 'https://bit.ly/3QfoCSG'),
                                    ],
                                    # [
                                    #     InlineKeyboardButton(text='alert', callback_data='alert')
                                    # ],
                                    [
                                        InlineKeyboardButton(text='Далі⏩', callback_data='Кнопки2')
                                    ]
                                ]



)

