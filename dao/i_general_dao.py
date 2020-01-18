from abc import abstractmethod, ABCMeta


class IGeneralDAO:
    __metaclass__ = ABCMeta

    @abstractmethod
    def find_all(self):
        # type: () -> []
        pass

    @abstractmethod
    def find_by_id(self, key):
        # type: (int) -> object
        pass

    @abstractmethod
    def create(self, obj):
        # type: (object) -> None
        pass

    @abstractmethod
    def update(self, key, obj):
        # type: (int, object) -> None
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
