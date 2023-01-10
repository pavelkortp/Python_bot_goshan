from aiogram import types
from keyboards.inline import ikb_menu, ikb_menu2
from loader import dp
from aiogram.types import CallbackQuery
from keyboards.default import kb_test

@dp.message_handler(text = "Інлайн меню")
async def show_inline_menu(message: types.Message):
    await message.answer('Інлайн кнопки нижче', reply_markup = ikb_menu)

@dp.callback_query_handler(text = 'Повідомлення')
async def send_message(call: CallbackQuery):
    await call.message.answer('Кнопки змінені', reply_markup=kb_test)

@dp.callback_query_handler(text = 'alert')
async def send_message(call: CallbackQuery):
    await call.answer('Кнопки змінені', show_alert=True)

@dp.callback_query_handler(text = 'Кнопки2')
async def send_message(call: CallbackQuery):
    await call.message.edit_reply_markup(ikb_menu2)

@dp.callback_query_handler(text = 'Кнопки1')
async def send_message(call: CallbackQuery):
    await call.message.edit_reply_markup(ikb_menu)