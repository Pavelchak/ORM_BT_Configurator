from ..i_role_dao import IRoleDAO
from ...general_dao import GeneralDAO
from domain.psoc6_gatt_profile import Role


class RoleDAO(GeneralDAO, IRoleDAO):
    _domain_type = Role
