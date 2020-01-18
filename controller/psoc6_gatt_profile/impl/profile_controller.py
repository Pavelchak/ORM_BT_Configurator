from service.psoc6_gatt_profile import profile_service
from ...general_controller import GeneralController
from ..i_profile_controller import IProfileController


class ProfileController(GeneralController, IProfileController):
    _service = profile_service
