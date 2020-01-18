from sqlalchemy import Column, Integer, String, ForeignKey
from ..base import Base, IGeneral


class Characteristic(Base, IGeneral):
    __tablename__ = 'prof_characteristic'
    id = Column(Integer, primary_key=True)
    type = Column(String(50), nullable=False)
    requirement = Column(String(30), nullable=False)
    prof_service_id = Column(Integer, ForeignKey('prof_service.id'), nullable=False)

    def __init__(self, type, requirement, prof_service_id):
        # type: (str, str, int) -> None
        self.type = type
        self.requirement = requirement
        self.prof_service_id = prof_service_id

    def __repr__(self):
        return "Characteristic('%s', '%s', '%s', '%s')" % (
            self.id, self.type, self.requirement, self.prof_service_id)

    def full_update(self, obj):
        self.type = obj.type
        self.requirement = obj.requirement
        self.prof_service_id = obj.prof_service_id
