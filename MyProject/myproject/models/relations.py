from .dbcreating import get_base
from sqlalchemy import Column, String, Integer, ForeignKey

Base = get_base()


class PersonRelations(Base):
    __tablename__ = "relations"
    id = Column(Integer, primary_key=True)
    #person1_id = Column(Integer, ForeignKey('person.id'))
    #guy1 = relationship("Test_guys", backref="guy_relations")
    #person2_id = Column(Integer, ForeignKey('person.id'))
    #guy = relationship("Test_guys", backref="guy_relations")
    relation = Column(String(50))

    def __repr__(self):
        return str(self.person1_id) + " " + str(self.person2_id) + " " + str(self.relation)
