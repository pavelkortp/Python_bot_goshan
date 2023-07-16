from aiogram import types
from aiogram.dispatcher.filters import Command

from filters import IsPrivate
from keyboards.default import kb_menu
from loader import dp


@dp.message_handler(IsPrivate(), Command("menu"))
async def menu(message: types.Message):
    await message.answer("Обери число з меню нижче", reply_markup=kb_menu)
