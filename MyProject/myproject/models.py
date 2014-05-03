from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    password = None

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    email = Column(String(50))


    # @staticmethod
    # def get_hashed_password(user, pwd=None):
    #     pwd = pwd or user.password
    #     if pwd is None:
    #         raise Exception("Hashed password of None")
    #     mhash = md5.new()
    #     mhash.update(pwd)
    #     mhash.update(user.salt)
    #     return mhash.hexdigest()

    def __init__(self, username, userfullname):
        self.name = username
        self.fullname = userfullname

    def __repr__(self):
        return "<User(%r, %r)>" % (self.name, self.fullname)

def register(login, email, password):
    if login and email and password:
        engine = create_engine('sqlite:///some.db')
        session = Session(bind=engine)
        query = session.query(User).filter(User.email == email)
        user = User(login, email)
        #send_email(email, password, 1)
        user.password = password
        session.add(user)
        session.commit()
        return user
    else:
        return False


def login(email, password):
    engine = create_engine('sqlite:///some.db')
    session = Session(bind=engine)
    query = session.query(User).filter(User.email == email)
    try:
        user = query.one()
        return user
    except NoResultFound:
        return None