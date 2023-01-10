from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_infomenu2 = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='ФІТ у телеграмі', url= 'https://t.me/fitknu'),    
                                    ],
                                    [
                                        InlineKeyboardButton(text='Сайт ФІТ', url = 'https://fit.knu.edu.ua/'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='ФІТ inst', url = 'https://www.instagram.com/fit.knu/'),  
                                    ],
                                    [
                                        InlineKeyboardButton(text='ФІТ discord', url = 'https://discord.gg/mnR95c8u5d') 
                                    ],
                                    [
                                        InlineKeyboardButton(text='⏪Назад', callback_data='Інфо1')
                                    ]
                                ]



) 