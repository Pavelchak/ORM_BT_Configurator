from service.psoc6_gatt_profile import role_service
from ...general_controller import GeneralController
from ..i_role_controller import IRoleController


class RoleController(GeneralController, IRoleController):
    _service = role_service
