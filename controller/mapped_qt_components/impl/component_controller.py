from service.mapped_qt_components import component_service
from ...general_controller import GeneralController
from ..i_component_controller import IComponentController


class ComponentController(GeneralController, IComponentController):
    _service = component_service
