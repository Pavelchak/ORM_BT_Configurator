from ..i_component_dao import IComponentDAO
from ...general_dao import GeneralDAO
from domain.mapped_qt_components import Component


class ComponentDAO(GeneralDAO, IComponentDAO):
    _domain_type = Component
