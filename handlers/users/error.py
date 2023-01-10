from aiogram import types
from loader import dp
from filters import IsPrivate

@dp.message_handler(IsPrivate())
async def command_error(message: types.Message):
    await message.answer(f'Команду {message.text} не знайдено')