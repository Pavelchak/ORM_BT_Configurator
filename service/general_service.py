from i_general_service import IGeneralService


class GeneralService(IGeneralService):
    _dao = None

    def find_all(self):
        return self._dao.find_all()

    def find_by_id(self, key):
        return self._dao.find_by_id(key)

    def create(self, obj):
        self._dao.create(obj)

    def update(self, key, obj):
        self._dao.update(key, obj)

    def patch(self, key, field_name, value):
        self._dao.patch(key, field_name, value)

    def delete(self, key):
        self._dao.delete(key)

    def delete_all(self):
        self._dao.delete_all()
