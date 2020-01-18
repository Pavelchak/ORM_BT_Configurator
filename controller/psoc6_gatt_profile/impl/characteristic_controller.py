from service.psoc6_gatt_profile import characteristic_service
from ...general_controller import GeneralController
from ..i_characteristic_controller import ICharacteristicController


class CharacteristicController(GeneralController, ICharacteristicController):
    _service = characteristic_service
