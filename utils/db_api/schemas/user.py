from sqlalchemy import Column, BigInteger, String, sql

from utils.db_api.db_gino import TimedBaseModel


class User(TimedBaseModel):
    """
    This class is model of user
    """
    __tablename__ = 'users'
    user_id = Column(BigInteger, primary_key=True)
    first_name = Column(String(200))
    last_name = Column(String(200))
    username = Column(String(50))
    status = Column(String(30))
    penis = Column(BigInteger())
    query: sql.select



