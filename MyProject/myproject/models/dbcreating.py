from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,)
from sqlalchemy import create_engine
from pyramid.threadlocal import get_current_request

Base = declarative_base()
DBSession = scoped_session(sessionmaker(), scopefunc=get_current_request)
engine = create_engine('sqlite:///gen_tree.db')
DBSession.configure(bind=engine)
Base.metadata.bind = engine
Base.metadata.create_all(engine)


def get_base():
    return Base

def get_db_session():
    return DBSession()
