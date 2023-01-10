from aiogram import types
from loader import dp

@dp.message_handler(text='Привіт')
async def command_hello(message: types.Message):
    await message.answer(f'Привіт, @{message.from_user.username}!')