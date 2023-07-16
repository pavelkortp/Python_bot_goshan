import random

from aiogram import types
from loader import dp

complaints_voice = []
with open("phrases/hate.txt", "r") as file:
    complaints_voice = file.read().split("1")


@dp.message_handler(content_types=['voice'])
async def get_user_voice(message: types.Voice):
    reaction_voice = random.choice(complaints_voice)
    await message.reply(reaction_voice)