import xml.etree.ElementTree as ET
from controller.mapped_qt_components import component_controller
from domain.mapped_qt_components import Component


class FormComponentDbLoader:
    __path_to_xml = None
    __i = 0

    def __init__(self, path_to_xml):
        self.__path_to_xml = path_to_xml

    def load_to_db_from_xml(self):
        print "...."
        tree = ET.parse(self.__path_to_xml)
        root = tree.getroot()
        root_element = root.findall("./execution/state/element")
        component_id = self.__save_to_component_table(root_element[0], None)
        self.get_child_elements(root_element[0], component_id)

    def __save_to_component_table(self, element, component_id):
        # element_tag = element.tag
        element_id = element.attrib['id']
        component_class = element.attrib['class']
        container = element.findtext(".realname").strip()
        text = None
        name = None
        title = None
        properties = element.findall("./properties/property")
        for property in properties:
            if property.attrib['name'] == "text":
                value = property.findtext(".string")
                if value is not None:
                    text = value.strip()
            elif property.attrib['name'] == "name":
                value = property.findtext(".string")
                if value is not None:
                    name = value.strip()
            elif property.attrib['name'] == "title":
                value = property.findtext(".string")
                if value is not None:
                    title = value.strip()
        component = Component(element_id, component_class, container, text, name, title, component_id)
        component_controller.create(component)
        return component.id

    def get_child_elements(self, parent_element, component_id):
        self.__i += 1
        if parent_element is not None:
            child_elements = parent_element.findall("./children/element")
            for element in child_elements:
                # save element
                child_component_id = self.__save_to_component_table(element, component_id)
                self.get_child_elements(element, child_component_id)
                if self.__i == 50:
                    break
