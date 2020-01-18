from dao.psoc6_gatt_profile import client_dao
from ...general_service import GeneralService
from ..i_client_service import IClientService


class ClientService(GeneralService, IClientService):
    _dao = client_dao
