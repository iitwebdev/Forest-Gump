from .dbcreating import get_base
from sqlalchemy import Column, String, Integer

Base = get_base()


class Person(Base):
    __tablename__ = "person"
    id = Column(Integer, primary_key=True)
    surname = Column(String(50))
    name = Column(String(50))
    middle_name = Column(String(50))
    #birth = Column(Integer)
    #end = Column(Integer)
    #bpl = Column(String(50))
