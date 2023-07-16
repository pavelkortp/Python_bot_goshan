from aiogram import types

from data.config import admins
from filters import IsPrivate
from loader import dp

commands = [
    types.BotCommand("start", "Запустити бота"),
    types.BotCommand("help", "Допомога"),
    types.BotCommand("anekdot", "Анекдот"),
    types.BotCommand("profile", "Отримати дані з бд"),
    types.BotCommand("penis", "Зіграти в гру песюн")
]


async def set_default_commands(dp):
    await dp.bot.set_my_commands(commands)


@dp.message_handler(IsPrivate(), chat_id=admins)
async def set_admin_commands(dp):
    commands.append(types.BotCommand("mail", "Розсилка"))
    await dp.bot.set_my_commands(commands)
