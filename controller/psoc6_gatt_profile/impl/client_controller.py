from service.psoc6_gatt_profile import client_service
from ...general_controller import GeneralController
from ..i_client_controller import IClientController


class ClientController(GeneralController, IClientController):
    _service = client_service
