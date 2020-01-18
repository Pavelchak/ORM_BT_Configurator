from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from ..base import Base, IGeneral


class Profile(Base, IGeneral):
    __tablename__ = 'prof_profile'
    id = Column(Integer, primary_key=True)
    type = Column(String(80), nullable=False)
    name = Column(String(50), nullable=False)
    abstract = Column(String(255))
    summary = Column(String)
    roles = relationship("Role", backref="profile")

    def __init__(self, type, name, abstract, summary):
        # type: (str, str, str, str) -> None
        self.type = type
        self.name = name
        self.abstract = abstract
        self.summary = summary

    def __repr__(self):
        return "Profile('%s', '%s', '%s', '%s', '%s')" % (self.id, self.type, self.name, self.abstract, self.summary)

    def full_update(self, obj):
        self.type = obj.type
        self.name = obj.name
        self.abstract = obj.abstract
        self.summary = obj.summary
