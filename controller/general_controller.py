from i_general_controller import IGeneralController


class GeneralController(IGeneralController):
    _service = None

    def find_all(self):
        return self._service.find_all()

    def find_by_id(self, key):
        return self._service.find_by_id(key)

    def create(self, obj):
        self._service.create(obj)

    def update(self, key, obj):
        self._service.update(key, obj)

    def patch(self, key, field_name, value):
        self._service.patch(key, field_name, value)

    def delete(self, key):
        self._service.delete(key)

    def delete_all(self):
        self._service.delete_all()
