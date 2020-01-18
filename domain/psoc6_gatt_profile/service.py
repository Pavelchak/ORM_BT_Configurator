from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from ..base import Base, IGeneral


class Service(Base, IGeneral):
    __tablename__ = 'prof_service'
    id = Column(Integer, primary_key=True)
    type = Column(String(50), nullable=False)
    declaration = Column(String(50), nullable=False)
    requirement = Column(String(30), nullable=False)
    prof_role_id = Column(Integer, ForeignKey('prof_role.id'), nullable=False)
    characteristics = relationship("Characteristic", backref="service")

    def __init__(self, type, declaration, requirement, prof_role_id):
        # type: (str, str, str, int) -> None
        self.type = type
        self.declaration = declaration
        self.requirement = requirement
        self.prof_role_id = prof_role_id

    def __repr__(self):
        return "Service('%s', '%s', '%s', '%s', '%s')" % (
            self.id, self.type, self.declaration, self.requirement, self.prof_role_id)

    def full_update(self, obj):
        self.type = obj.type
        self.declaration = obj.declaration
        self.requirement = obj.requirement
        self.prof_role_id = obj.prof_role_id
