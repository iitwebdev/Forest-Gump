from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from myproject.bd_test import User

engine = create_engine('sqlite:///some.db')
session = Session(bind=engine)

our_user = session.query(User).order_by(User.id).first()
print(our_user.name)
