import random

from aiogram import types

from loader import dp
from utils.db_api import quick_commands as commands


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    """
    This method created new user and greets they. Or grate already registered user.
    :param message: message with command 'start'.
    :return: None.
    """
    try:
        user = await commands.select_user(message.from_user.id)
        if user.status == 'active':
            await message.answer(f'Привіт {user.first_name}\n'
                                 f'Ти вже зареєстрований')
        elif user.status == 'baned':
            await message.answer('Тебе заблоковано')
    except Exception:
        await commands.add_user(user_id=message.from_user.id,
                                first_name=message.from_user.first_name,
                                last_name=message.from_user.last_name,
                                username=message.from_user.username,
                                status='active',
                                penis=random.randrange(0, 10))
        await message.answer('Тебе зареєстровано')


@dp.message_handler(commands='profile')
async def profile(message: types.Message):
    """
    This method send to user all data about him/her.
    :param message: message with command /profile.
    :return: None.
    """
    user = await commands.select_user(message.from_user.id)
    await message.reply(f'Твій айді - {user.user_id}\n'
                        f'first_name - {user.first_name}\n'
                        f'last_name - {user.last_name}\n'
                        f'username - {user.username}\n'
                        f'status - {user.status}\n'
                        f'penis - {user.penis}')
