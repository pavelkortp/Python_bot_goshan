from aiogram import types
from loader import dp
from keyboards.inline import ikb_infomenu1, ikb_infomenu2
from aiogram.types import CallbackQuery

@dp.message_handler(text=['/info', '/info@M4karBot'])
async def command_help(message: types.Message):
    await message.answer(f'Привіт, мене звати Гошан. Я - бот, що еволюціонує!\n'
                        f'Нижче кнопки з корисними посиланнями', reply_markup=ikb_infomenu1)

@dp.callback_query_handler(text = 'Інфо1')
async def send_message(call: CallbackQuery):
    await call.message.edit_reply_markup(ikb_infomenu1)

@dp.callback_query_handler(text = 'Інфо2')
async def send_message(call: CallbackQuery):
    await call.message.edit_reply_markup(ikb_infomenu2)
