from loader import dp
from aiogram.dispatcher.filters import Command
from aiogram import types
from filters import IsPrivate
from keyboards.default import kb_menu

@dp.message_handler(IsPrivate(), Command("menu"))
async def menu(message: types.Message):
    await message.answer("Обери число з меню нижче", reply_markup=kb_menu)
