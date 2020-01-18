from dao.psoc6_gatt_profile import service_dao
from ...general_service import GeneralService
from ..i_service_service import IServiceService


class ServiceService(GeneralService, IServiceService):
    _dao = service_dao
