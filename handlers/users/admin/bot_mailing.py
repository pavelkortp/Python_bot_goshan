from asyncio import sleep

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from data.config import admins
from filters import IsPrivate
from keyboards.inline import ikb_menu
from keyboards.inline import ikb_menu2
from loader import dp
from states import bot_mailing
from utils.db_api import quick_commands as commands


@dp.message_handler(IsPrivate(), text='/mail', chat_id=admins)
async def start_mailing(message: types.Message):
    await message.answer(f'Додайте текст розсилки:')
    await bot_mailing.text.set()


@dp.message_handler(IsPrivate(), state=bot_mailing.text)
async def mailing_text(message: types.Message, state: FSMContext):
    answer = message.text
    markup = InlineKeyboardMarkup(row_width=2,
                                  inline_keyboard=[
                                      [
                                          InlineKeyboardButton(text='Додати медіафайл', callback_data='add_media'),
                                          InlineKeyboardButton(text='Далі', callback_data='next'),
                                          InlineKeyboardButton(text='Відмінити', callback_data='quit')
                                      ]
                                  ])
    await state.update_data(text=answer)
    await message.answer(text=answer, reply_markup=markup)
    await bot_mailing.state.set()


@dp.callback_query_handler(text='next', state=bot_mailing.state)
async def start(call: types.CallbackQuery, state=FSMContext):
    users = await commands.select_all_users()
    data = await state.get_data()
    text = data.get('text')
    await state.finish()
    for user in users:
        try:
            await dp.bot.send_message(chat_id=user.user_id, text=text, reply_markup=ikb_menu2)
        except Exception:
            await call.message.answer('mailing has NOT been completed')
    await call.message.answer('mailing has been completed')


@dp.callback_query_handler(text='add_media', state=bot_mailing.state)
async def add_media(call: types.CallbackQuery):
    await call.message.answer('Надішліть медіа')
    await bot_mailing.media.set()


@dp.message_handler(IsPrivate(), state=bot_mailing.media, content_types=types.ContentType.ANY)
async def mailing_text(message: types.Message, state: FSMContext):
    photo_file_id = message.photo[-1].file_id
    await state.update_data(photo=photo_file_id)
    data = await state.get_data()
    text = data.get('text')
    photo = data.get('photo')
    markup = InlineKeyboardMarkup(row_width=2,
                                  inline_keyboard=[
                                      [
                                          InlineKeyboardButton(text='Далі', callback_data='next'),
                                          InlineKeyboardButton(text='Відмінити', callback_data='quit')
                                      ]
                                  ])
    await message.answer_photo(photo=photo, caption=text, reply_markup=markup)


@dp.callback_query_handler(text='next', state=bot_mailing.media)
async def start(call: types.CallbackQuery, state=FSMContext):
    users = await commands.select_all_users()
    print(users)
    data = await state.get_data()
    text = data.get('text')
    photo = data.get('photo')
    await state.finish()
    for user in users:
        try:
            await dp.bot.send_photo(chat_id=user.user_id, photo=photo, caption=text, reply_markup=ikb_menu)
            await sleep(0.25)
        except Exception:
            pass
    await call.message.answer('mailing has been completed')


@dp.message_handler(IsPrivate(), state=bot_mailing.media)
async def no_photo(message: types.Message):
    markup = InlineKeyboardMarkup(row_width=2,
                                  inline_keyboard=[
                                      [
                                          InlineKeyboardButton(text='Відмінити', callback_data='quit')
                                      ]
                                  ])
    await message.answer('Please send a photo', reply_markup=markup)


@dp.callback_query_handler(text='quit', state=[bot_mailing.text, bot_mailing.media, bot_mailing.state])
async def quit(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.answer('Mailing has been canceled')
