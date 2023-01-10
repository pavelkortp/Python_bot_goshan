from distutils.command.config import config
from loader import dp
from aiogram import types
from data import config
from utils.misc import rate_limit
from filters import IsGroup

@rate_limit(limit=0, key='groups')
@dp.message_handler(IsGroup())
async def check_messages(message: types.Message):
    text = message.text.lower().replace(' ', '')

    for banned_message in config.banned_messages:
        if banned_message in text:
            # бот видаляє повідомлення в групі з бансловом
            await message.delete()


