from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class IsPrivate(BoundFilter):
    """
    This class are custom filter which check if current chat is Private.
    """
    async def check(self, message: types.Message):
        return message.chat.type == types.ChatType.PRIVATE
