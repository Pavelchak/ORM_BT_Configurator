from ..i_gap_role_dao import IGapRoleDAO
from ...general_dao import GeneralDAO
from domain.psoc6_gatt_profile import GapRole


class GapRoleDAO(GeneralDAO, IGapRoleDAO):
    _domain_type = GapRole
