from dao.psoc6_gatt_profile import role_dao
from ...general_service import GeneralService
from ..i_role_service import IRoleService\


class RoleService(GeneralService, IRoleService):
    _dao = role_dao
