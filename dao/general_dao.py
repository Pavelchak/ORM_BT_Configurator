from i_general_dao import IGeneralDAO
from domain import session


class GeneralDAO(IGeneralDAO):
    _domain_type = None

    def find_all(self):
        return session.query(self._domain_type).all()

    def find_by_id(self, key):
        return session.query(self._domain_type).get(key)

    def create(self, obj):
        session.add(obj)
        session.commit()

    def update(self, key, obj):
        domain_obj = session.query(self._domain_type).get(key)
        domain_obj.full_update(obj)
        session.commit()

    def patch(self, key, field_name, value):
        domain_obj = session.query(self._domain_type).get(key)
        setattr(domain_obj, field_name, value)
        session.commit()

    def delete(self, key):
        domain_obj = session.query(self._domain_type).get(key)
        session.delete(domain_obj)
        session.commit()

    def delete_all(self):
        session.query(self._domain_type).delete()
        session.commit()
