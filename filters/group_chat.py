from tokenize import group
from aiogram.dispatcher.filters import BoundFilter
from aiogram import types

class IsGroup(BoundFilter):
    async def check(self, message: types.Message):
        group_types = [types.ChatType.GROUP, types.ChatType.SUPERGROUP]
        return message.chat.type in group_types