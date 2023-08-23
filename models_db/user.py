from sqlalchemy import Column, Integer, String

from database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key = True, autoincrement = True)
    first_name = Column('first_name', String)
    last_name = Column('last_name', String)
    username = Column('username', String, unique = True)
    email = Column('email', String, unique = True)
    balance = Column('balance', Integer)
