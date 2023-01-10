from aiogram import types
from loader import dp
from utils.db_api import quick_commands as commands
from utils.misc.throttling import rate_limit
from filters import IsGroup, IsPrivate

@rate_limit(limit=3)
@dp.message_handler(text=['/start', '/start@M4karBot'])
async def command_start(message: types.Message):
    try:
        user = await commands.select_user(message.from_user.id)
        if user.status == 'active':
            await message.answer(f'Привіт {user.first_name}\n'
                                f'Ти вже зареєстрований')
        elif user.status == 'baned':
            await message.answer('Тебе заблоковано')
    except Exception:
        await commands.add_user(user_id=message.chat.id,
                                first_name = message.from_user.first_name,
                                last_name = message.from_user.last_name,
                                username = message.from_user.username,
                                status = 'active')
        await message.answer('Тебе зареєстровано')

@rate_limit(limit=5)
@dp.message_handler(text='/ban')
async def get_ban(message: types.Message):
    await commands.update_status(user_id = message.from_user.id, status='baned')
    await message.answer('Тебе заблоковано')

@rate_limit(limit=5)
@dp.message_handler( text='/unban')
async def get_unban(message: types.Message):
    await commands.update_status(user_id = message.from_user.id, status='active')
    await message.answer('Тебе розблоковано')

@rate_limit(limit=5)
@dp.message_handler(text='/profile')
async def profile(message: types.Message):
    user = await commands.select_user(message.from_user.id)
    await message.answer(f'Твій айді - {user.user_id}\n'
                            f'first_name - {user.first_name}\n'
                            f'last_name - {user.last_name}\n'
                            f'username - {user.username}\n'
                            f'status - {user.status}')
