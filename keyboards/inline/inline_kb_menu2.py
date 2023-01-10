from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_menu2 = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Donate', url= 'https://bit.ly/3ARKJbQ'),
                                        InlineKeyboardButton(text='Посилання', url = 'https://bit.ly/3QfoCSG'),    
                                    ],
                                    [
                                        InlineKeyboardButton(text='Долучитися', url = 'https://t.me/+s0935RC0yMBjYjRi')
                                    ],
                                    [
                                        InlineKeyboardButton(text='⏪Назад', callback_data='Кнопки1')
                                    ]
                                ]



)