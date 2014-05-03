from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    _password = None

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    email = Column(String(50))

    @property
    def password(self):
        """ Gets a transient password """
        return self._password

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

ed_user = User('ed', 'Edward Jones')

from sqlalchemy import create_engine
import os

if os.path.exists("some.db"):
    os.remove("some.db")
engine = create_engine('sqlite:///some.db')
Base.metadata.create_all(engine)

from sqlalchemy.orm import Session
session = Session(bind=engine)

### slide::
# new objects are placed into the Session using add().
session.add(ed_user)

### slide:: pi
# the Session will *flush* *pending* objects
# to the database before each Query.

our_user = session.query(User).filter_by(name='ed').first()
print(our_user.id)

session.add_all([
    User('wendy', 'Wendy Weathersmith'),
    User('mary', 'Mary Contrary'),
    User('fred', 'Fred Flinstone')
])

session.commit()

session.close()

