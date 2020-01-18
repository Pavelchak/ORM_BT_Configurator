from service.psoc6_gatt_profile import gap_role_service
from ...general_controller import GeneralController
from ..i_gap_role_controller import IGapRoleController


class GapRoleController(GeneralController, IGapRoleController):
    _service = gap_role_service
