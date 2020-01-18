from ..i_service_dao import IServiceDAO
from ...general_dao import GeneralDAO
from domain.psoc6_gatt_profile import Service


class ServiceDAO(GeneralDAO, IServiceDAO):
    _domain_type = Service
