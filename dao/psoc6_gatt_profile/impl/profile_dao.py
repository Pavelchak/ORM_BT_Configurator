from ..i_profile_dao import IProfileDAO
from ...general_dao import GeneralDAO
from domain.psoc6_gatt_profile import Profile


class ProfileDAO(GeneralDAO, IProfileDAO):
    _domain_type = Profile
