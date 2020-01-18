from dao.psoc6_gatt_profile import gap_role_dao
from ...general_service import GeneralService
from ..i_gap_role_service import IGapRoleService


class Gap_Role_Service(GeneralService, IGapRoleService):
    _dao = gap_role_dao
