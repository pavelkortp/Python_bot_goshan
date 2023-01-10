from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_infomenu1 = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Розклад пар🔔', url= 'https://bit.ly/3xjwYlh'),    
                                    ],
                                    [
                                        InlineKeyboardButton(text='Підтримка🙋', url = 'https://t.me/knu_univer_zz'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='Cтароста👨‍🎓', url = 'https://t.me/Haharon'), 
                                    ],
                                    [
                                        InlineKeyboardButton(text='Заст Старости👨🏼‍🎓', url = 'https://t.me/bobbbiiiii'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='Далі⏩', callback_data='Інфо2')
                                    ]
                                ]



)