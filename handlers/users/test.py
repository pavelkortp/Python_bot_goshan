from aiogram import types
from loader import dp
from keyboards.default import kb_test
@dp.message_handler(text='Будь-що')
async def command_start(message: types.Message):
    await message.answer(f'Привіт, @{message.from_user.username}\n'
                        f'Тут має бути якийсь текст', reply_markup=kb_test)