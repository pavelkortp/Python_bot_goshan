from aiogram import types
from loader import dp

from filters import IsPrivate
from utils.misc.throttling import rate_limit

@rate_limit(limit=3)
@dp.message_handler(IsPrivate(), text='/start')
async def command_start(message: types.Message):
    await message.answer(f'Привіт, @{message.from_user.username}, мене звати Гошан. Я - бот, що еволюціонує!\n'
                        f'Твій айді: {message.from_user.id}')