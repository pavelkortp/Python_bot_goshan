import re
from filters.private_chat import IsPrivate
from loader import dp
from aiogram.dispatcher.filters import Command
from aiogram import types
from states import register
from aiogram.dispatcher import FSMContext
from keyboards.default import kb_menu

@dp.message_handler(IsPrivate(), Command('register'))
async def register_(message: types.Message):
    from aiogram.types import ReplyKeyboardMarkup
    from aiogram.types import KeyboardButton
    name = ReplyKeyboardMarkup(
    keyboard=[
                [
                    KeyboardButton(text =f'{message.from_user.first_name}'),
                ],
            ],
        resize_keyboard=True
    )
    await message.answer('Привіт ти почав реєстрацію,\nЯк тебе звати?', reply_markup=name)
    await register.test1.set()

@dp.message_handler(state=register.test1)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(test1 = answer)
    await message.answer(f'{answer}, скільки тобі років?')
    await register.test2.set()

@dp.message_handler(state=register.test2)
async def state2(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(test2 = answer)
    data = await state.get_data()
    name = data.get('test1')
    years = data.get('test2')
    await message.answer(f"Реєстрація пройшла успішно\n"
                        f"Твоє ім'я: {name}\n"
                        f"Тобі {years} років", reply_markup=kb_menu)
    await state.finish()
    