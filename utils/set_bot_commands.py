from aiogram import types
from filters import IsPrivate

async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand('start', 'Запустити бота'),
        types.BotCommand('help', 'Допомога'),
        types.BotCommand('anekdot', 'Анекдот'),
        types.BotCommand('profile', 'Отримати дані з бд'),
    ])
