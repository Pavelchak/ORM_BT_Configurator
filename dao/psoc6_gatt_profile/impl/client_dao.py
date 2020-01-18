from ..i_client_dao import IClientDAO
from ...general_dao import GeneralDAO
from domain.psoc6_gatt_profile import Client


class ClientDAO(GeneralDAO, IClientDAO):
    _domain_type = Client
