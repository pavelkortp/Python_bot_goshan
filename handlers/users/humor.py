import random

from aiogram import types

from loader import dp

anecdotes = []

with open("phrases/jokes.txt", "r") as file:
    anecdotes = list(file.read().split("₴"))


@dp.message_handler(text=['/anekdot', '/anekdot@M4karBot'])
async def get_anekdot(message: types.Message):
    joke = random.choice(anecdotes)
    await message.answer(text=joke)


@dp.message_handler(text=['Да', 'да'])
async def mem(message: types.Message):
    await message.answer("БАРАДА")
