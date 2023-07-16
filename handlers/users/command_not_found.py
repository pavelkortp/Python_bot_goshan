from aiogram import types

from filters import IsPrivate
from loader import dp


@dp.message_handler(IsPrivate())
async def command_error(message: types.Message):
    await message.answer(f'Команду {message.text} не знайдено')
