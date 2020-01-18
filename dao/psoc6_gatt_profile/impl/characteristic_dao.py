from ..i_characteristic_dao import ICharacteristicDAO
from ...general_dao import GeneralDAO
from domain.psoc6_gatt_profile import Characteristic


class CharacteristicDAO(GeneralDAO, ICharacteristicDAO):
    _domain_type = Characteristic
