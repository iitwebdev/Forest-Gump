from sqlalchemy.orm.exc import NoResultFound
from .user import User
from .person import Person
from .relations import PersonRelations
from .dbcreating import get_db_session, get_base


def register(name, email, password, sex):
    if name and email and password:
        session = get_db_session()
        query = session.query(User).filter(User.email == email)
        try:
            query.one()
            return False
        except NoResultFound:
            u = User(name=name, email=email, sex=sex, password=password)
            session.add(u)
            session.commit()
            return u
    else:
        return False


def add_person(surname, name, middle_name, birth, end, bpl):
    if surname and name and middle_name and birth and end and bpl:
        session = get_db_session()
        query = session.query(Person).filter(Person.name == name and Person.surname == surname
                                             and Person.middle_name == middle_name)
        try:
            query.one()
            return False
        except NoResultFound:
            p = Person(name=name, surname=surname, middle_name=middle_name, birth=birth, end=end, bpl=bpl)
            session.add(p)
            session.commit()
            return p
    else:
        return False


def add_persons_relation(person1_name, person2_name, relation):
    if person1_name and person2_name and relation:
        session = get_db_session()
        person1 = session.query(Person).filter(Person.name == person1_name).one()
        person2 = session.query(Person).filter(Person.name == person2_name).one()

        query = session.query(PersonRelations).filter(PersonRelations.person1_id == person1.id
                                                      and PersonRelations.person2_id == person2.id)
        try:
            query.one()
            return False
        except NoResultFound:
            rel = PersonRelations(person1_id=person1.id, person2_id=person2.id, relation=relation)
            session.add(rel)
            session.commit()
            return rel
    else:
        return False


def login(email, password):
    session = get_db_session()
    query = session.query(User).filter(User.email == email and User.password == password)
    try:
        u = query.one()
        return u
    except NoResultFound:
        return None


def all_users():
    session = get_db_session()
    Base = get_base()
    if User not in Base.metadata.tables:
        return []
    for u in session.query(User):
        print(u.id, u.name, u.email)


def all_persons():
    session = get_db_session()
    persons = []
    Base = get_base()
    if Person not in Base.metadata.tables:
        return []
    for p in session.query(Person):
        persons.append(p.name)
    return persons


def all_relations():
    session = get_db_session()
    Base = get_base()
    if PersonRelations not in Base.metadata.tables:
        return {}
    rs = {}
    for rel in session.query(PersonRelations):
        person1 = session.query(PersonRelations).filter_by(id=rel.person1_id).one()
        person2 = session.query(PersonRelations).filter_by(id=rel.person2_id).one()
        rs[rel.relation] = [person1.name, person2.name]
    return rs


def del_all_users():
    session = get_db_session()
    for u in session.query(User):
        session.delete(u)
    session.commit()


def del_user(username):
    session = get_db_session()
    try:
        user1 = session.query(User).filter_by(name=username).first()
        session.delete(user1)
        session.commit()
    except Exception:
        print(Exception)


def del_all_persons():
    session = get_db_session()
    for p in session.query(Person):
        session.delete(p)
    session.commit()


def del_person(username):
    session = get_db_session()
    guy = session.query(Person).filter_by(name=username).first()
    session.delete(guy)
    session.commit()


def del_all_rels():
    session = get_db_session()
    for pr in session.query(PersonRelations):
        session.delete(pr)
    session.commit()


def get_user(id_, request):
    #request for autorization, don't delete
    session = get_db_session()
    if not id_:
        raise NoResultFound
    u = session.query(User).get(id_)
    if u:
        return session.query(User).get(id_)
    else:
        raise NoResultFound



