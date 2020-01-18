from dao.psoc6_gatt_profile import characteristic_dao
from ...general_service import GeneralService
from ..i_characteristic_service import ICharacteristicService


class CharacteristicService(GeneralService, ICharacteristicService):
    _dao = characteristic_dao
