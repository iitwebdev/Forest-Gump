from .dbcreating import get_base
from sqlalchemy import Column, String, Integer

Base = get_base()


class User(Base):
    __tablename__ = "user"
    #_password = Column(String(50))
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    email = Column(String(50))
    sex = Column(String(10))
