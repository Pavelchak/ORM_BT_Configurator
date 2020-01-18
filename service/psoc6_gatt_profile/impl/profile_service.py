from dao.psoc6_gatt_profile import profile_dao
from ...general_service import GeneralService
from ..i_profile_service import IProfileService


class ProfileService(GeneralService, IProfileService):
    _dao = profile_dao
