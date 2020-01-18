from sqlalchemy import Column, Integer, String, ForeignKey
from ..base import Base, IGeneral


class GapRole(Base, IGeneral):
    __tablename__ = 'prof_gap_role'
    id = Column(Integer, primary_key=True)
    gap_role = Column(String(40), nullable=False)
    prof_role_id = Column(Integer, ForeignKey('prof_role.id'), nullable=False)

    def __init__(self, gap_role, prof_role_id):
        # type: (str, int) -> None
        self.gap_role = gap_role
        self.prof_role_id = prof_role_id

    def __repr__(self):
        return "GapRole('%s', '%s', '%s')" % (
            self.id, self.gap_role, self.prof_role_id)

    def full_update(self, obj):
        self.gap_role = obj.gap_role
        self.prof_role_id = obj.prof_role_id
