from aiogram import types
from loader import dp
from keyboards.inline import ikb_menu2, ikb_menu

@dp.message_handler(text='10')
async def buttons_test(message: types.Message):
    await message.answer(f'Привіт, @{message.from_user.username}, мене звати Гошан. Я - бот, що еволюціонує!\n'
                        f'Ти обрав число {message.text}')

@dp.message_handler(text='11')
async def buttons_test(message: types.Message):
    await message.answer(f'Привіт, @{message.from_user.username}, мене звати Гошан. Я - бот, що еволюціонує!\n'
                        f'Ти обрав число {message.text}')

@dp.message_handler(text='100')
async def buttons_test(message: types.Message):
    await message.answer(f'Привіт, @{message.from_user.username}, мене звати Гошан. Я - бот, що еволюціонує!\n'
                        f'Ти обрав число {message.text}')  

@dp.message_handler(text='Інлайн меню')
async def buttons_test(message: types.Message):
    await message.answer('Інлайн кнопки нижче', reply_markup = ikb_menu)                     