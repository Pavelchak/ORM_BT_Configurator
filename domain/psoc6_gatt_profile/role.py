from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from ..base import Base, IGeneral


class Role(Base, IGeneral):
    __tablename__ = 'prof_role'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    prof_profile_id = Column(Integer, ForeignKey('prof_profile.id'), nullable=False)
    gap_roles = relationship("GapRole", backref="role")
    clients = relationship("Client", backref="role")
    services = relationship("Service", backref="role")

    def __init__(self, name, prof_profile_id):
        # type: (str, int) -> None
        self.name = name
        self.prof_profile_id = prof_profile_id

    def __repr__(self):
        return "Role('%s', '%s', '%s',\n '%s')" % (self.id, self.name, self.prof_profile_id, self.profile)

    def full_update(self, obj):
        self.name = obj.name
        self.prof_profile_id = obj.prof_profile_id
