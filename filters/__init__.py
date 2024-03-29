from aiogram import Dispatcher
from .private_chat import IsPrivate
from .group_chat import IsGroup


def setup(dp: Dispatcher):
    dp.filters_factory.bind(IsPrivate)
    dp.filters_factory.bind(IsGroup)
