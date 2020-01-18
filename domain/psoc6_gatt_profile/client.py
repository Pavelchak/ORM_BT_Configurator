from sqlalchemy import Column, Integer, String, ForeignKey
from ..base import Base, IGeneral


class Client(Base, IGeneral):
    __tablename__ = 'prof_client'
    id = Column(Integer, primary_key=True)
    type = Column(String(50), nullable=False)
    requirement = Column(String(30), nullable=False)
    prof_role_id = Column(Integer, ForeignKey('prof_role.id'), nullable=False)

    def __init__(self, type, requirement, prof_role_id):
        # type: (str, str, int) -> None
        self.type = type
        self.requirement = requirement
        self.prof_role_id = prof_role_id

    def __repr__(self):
        return "Client('%s', '%s', '%s', '%s')" % (
            self.id, self.type, self.requirement, self.prof_role_id)

    def full_update(self, obj):
        self.type = obj.type
        self.requirement = obj.requirement
        self.prof_role_id = obj.prof_role_id
