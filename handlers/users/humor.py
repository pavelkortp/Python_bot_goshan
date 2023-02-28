from asyncore import read
from aiogram import types
from aiogram.types import InputFile
from loader import dp, bot
from random import randrange
from phrases import *


anekdots = []
async def func(anekdots):
    return randrange(0, len(anekdots))


@dp.message_handler(text = ['/anekdot', '/anekdot@M4karBot'] )
async def get_anekdot(message: types.Message):
    rofl = anekdots[int(func(anekdots))]
    await message.answer(text = rofl)

@dp.message_handler(text = ['Да', 'да'] )
async def mem(message: types.Message):
    await message.answer("БАРАДА")
# ['/anekdot', '/anekdot@M4karBot']

