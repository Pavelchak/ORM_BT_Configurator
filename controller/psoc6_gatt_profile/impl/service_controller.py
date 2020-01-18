from service.psoc6_gatt_profile import service_service
from ...general_controller import GeneralController
from ..i_service_controller import IServiceController


class ServiceController(GeneralController, IServiceController):
    _service = service_service
