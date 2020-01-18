from dao.mapped_qt_components import component_dao
from ...general_service import GeneralService
from ..i_component_service import IComponentService


class ComponentService(GeneralService, IComponentService):
    _dao = component_dao
