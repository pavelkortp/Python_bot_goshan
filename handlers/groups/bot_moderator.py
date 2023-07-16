from distutils.command.config import config

from aiogram import types

from data import config
from filters import IsGroup
from loader import dp


@dp.message_handler(IsGroup())
async def check_messages(message: types.Message):
    """
    This method delete all messages which contains ban-word.
    :param message: text message.
    :return:
    """
    text = message.text.lower().replace(' ', '')

    for banned_message in config.banned_messages:
        if banned_message in text:
            # бот видаляє повідомлення в групі з бансловом
            await message.delete()
