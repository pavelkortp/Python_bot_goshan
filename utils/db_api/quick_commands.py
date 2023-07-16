from asyncpg import UniqueViolationError

from utils.db_api.schemas.user import User


async def add_user(user_id: int, first_name: str, last_name: str, username: str, status: str,
                   penis: int = 0) -> bool:
    """
    This method add user to db.
    :param user_id: id of user.
    :param first_name: first name of user.
    :param last_name: last name of user.
    :param username: username.
    :param status: user status (active or banned).
    :param penis: length of user penis.
    :return: True if user successfully added to db or false otherwise.
    """
    try:
        user = User(user_id=user_id,
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    status=status,
                    penis=penis)
        await user.create()
        return True
    except UniqueViolationError:
        return False


async def select_all_users() -> list:
    """
    This method select all user from db and return it as list.
    :return: list of users.
    """
    users = await User.query.gino.all()
    return users


async def select_user(user_id: int) -> User:
    """
    This method select first user from db with user_id.
    :param user_id: id of current user.
    :return: new User()
    """
    user = await User.query.where(User.user_id == user_id).gino.first()
    return user


async def update_status(user_id: int, status: str):
    user = await select_user(user_id)
    await user.update(status=status).apply()


async def update_penis(user_id: int, penis: int):
    """
    This method update user len of penis in db.
    :param user_id: id of user.
    :param penis: new len of penis.
    :return:
    """
    user = await select_user(user_id)
    await user.update(penis=penis).apply()
