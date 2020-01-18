from abc import abstractmethod, ABCMeta


class IGeneralService:
    __metaclass__ = ABCMeta

    @abstractmethod
    def find_all(self):
        pass

    @abstractmethod
    def find_by_id(self, key):
        pass

    @abstractmethod
    def create(self, obj):
        pass

    @abstractmethod
    def update(self,key, obj):
        pass

    @abstractmethod
    def patch(self, key, field_name, value):
        # type: (int, str, object) -> None
        pass

    @abstractmethod
    def delete(self, key):
        # type: (int) -> None
        pass

    @abstractmethod
    def delete_all(self):
        # type: () -> None
        pass