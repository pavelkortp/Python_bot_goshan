import random

from aiogram import types

from filters import IsGroup
from loader import dp
from utils.db_api import quick_commands as commands


@dp.message_handler(IsGroup(), text='/penis')
async def command_penis(message: types.Message) -> bool:
    """
    This method is penis chat game where user send /penis and get a new penis size.
    :param message: message which contains only command "/penis"
    :return: True if user penis are changed completely,  otherwise false.
    """
    delta = random.randrange(-10, 10)
    try:
        current_user_id = message.from_user.id
        user = await commands.select_user(current_user_id)
        if delta < 0:
            user.penis = user.penis + delta
            await message.reply(f'{user.first_name}\n'
                                f'Твій пісун скоротився на {abs(delta)} см, тепер його довжина становить {user.penis} cм.')
        else:
            user.penis = user.penis + delta
            await message.reply(f'{user.first_name}\n'
                                f'Твій пісун виріс на {abs(delta)} см, тепер його довжина становить {user.penis} cм.')
        await commands.update_penis(user_id=current_user_id, penis=user.penis)
        return True
    except AttributeError:
        await message.reply(f'Спочатку зареєструйся, щоб грати в цю чудову гру!')
        return False


@dp.message_handler(IsGroup(), text='/top')
async def command_top(message: types.Message) -> bool:
    """
    This method send to user top of users penis.
    :param message: message with command 'top'
    :return:
    """
    try:
        current_user = message.from_user.first_name
        users = sorted(await commands.select_all_users(), key=lambda user: user.penis, reverse=True)
        formatted_users = ""
        for i, user in enumerate(users, start=1):
            formatted_users += f'{i} - {user.first_name}\n'
        await message.reply(f'{current_user}\n',
                            formatted_users)
    except Exception:
        print(Exception)
