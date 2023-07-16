from aiogram import types
from aiogram.types import CallbackQuery

from keyboards.inline import ikb_infomenu1, ikb_infomenu2
from loader import dp


@dp.message_handler(commands='help')
async def command_help(message: types.Message):
    """
    This method send to user useful info.
    :param message: message with command 'help'.
    :return: None.
    """
    await message.answer(f'Привіт, мене звати Гошан. Я - бот, що еволюціонує!\n'
                         f'Нижче кнопки з корисними посиланнями', reply_markup=ikb_infomenu1)


@dp.callback_query_handler(text='Інфо1')
async def send_message(call: CallbackQuery):
    await call.message.edit_reply_markup(ikb_infomenu1)


@dp.callback_query_handler(text='Інфо2')
async def send_message(call: CallbackQuery):
    await call.message.edit_reply_markup(ikb_infomenu2)
