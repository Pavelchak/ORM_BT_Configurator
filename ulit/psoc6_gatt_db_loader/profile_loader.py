import os
import xml.etree.ElementTree as ET
from controller.psoc6_gatt_profile import profile_controller, role_controller, gap_role_controller, client_controller, \
    service_controller, characteristic_controller
from domain.psoc6_gatt_profile import Characteristic, Client, GapRole, Profile, Role, Service


class GattDbLoader:
    __path_to_xmls = None

    def __init__(self, path_to_xmls):
        self.__path_to_xmls = path_to_xmls

    def __get_list_xml_files(self):
        all_files = os.listdir(self.__path_to_xmls)
        xml_files = list()
        for any_file in all_files:
            file_name, file_extension = os.path.splitext(any_file)
            if file_extension == ".xml":
                xml_files.append(self.__path_to_xmls + '/' + any_file)
        return xml_files

    def load_to_db_from_xml(self):
        xml_files = self.__get_list_xml_files()
        for xml_file in xml_files:
            tree = ET.parse(xml_file)
            root = tree.getroot()
            profile_id = self.__save_to_profile_table(root)
            roles = root.findall("./Role")
            for role in roles:
                role_id = self.__save_to_role_table(role, profile_id)
                for element_in_role in role:
                    if element_in_role.tag == "GapRole":
                        self.__save_to_gap_role_table(element_in_role, role_id)
                    elif element_in_role.tag == "Client":
                        self.__save_to_client_table(element_in_role, role_id)
                    elif element_in_role.tag == "Service":
                        service_id = self.__save_to_service_table(element_in_role, role_id)
                        for element_in_service in element_in_role:
                            if element_in_service.tag == "Characteristic":
                                self.__save_to_characteristic_table(element_in_service, service_id)

    def __save_to_profile_table(self, root_element):
        # type: (ET) -> int
        type = root_element.attrib['type']
        name = root_element.attrib['name']
        abstract = root_element.findtext(".InformativeText/Abstract").strip()
        summary = root_element.findtext(".InformativeText/Abstract").strip()
        profile = Profile(type, name, abstract, summary)
        profile_controller.create(profile)
        return profile.id

    def __save_to_role_table(self, role_element, profile_id):
        # type: (ET, int) -> int
        name = role_element.attrib['name']
        role = Role(name, profile_id)
        role_controller.create(role)
        return role.id

    def __save_to_gap_role_table(self, gap_role_element, role_id):
        # type: (ET, int) -> int
        name = gap_role_element.text.strip()
        gap_role = GapRole(name, role_id)
        gap_role_controller.create(gap_role)
        return gap_role.id

    def __save_to_client_table(self, client_element, role_id):
        # type: (ET, int) -> int
        type = client_element.attrib['type']
        requirement = client_element[0].text.strip()
        client = Client(type, requirement, role_id)
        client_controller.create(client)
        return client.id

    def __save_to_service_table(self, service_element, role_id):
        # type: (ET, int) -> int
        type = service_element.attrib['type']
        declaration = None
        requirement = None
        for element in service_element:
            if element.tag == "Declaration":
                declaration = element.text
            elif element.tag == "Requirement":
                requirement = element.text
        service = Service(type, declaration, requirement, role_id)
        service_controller.create(service)
        return service.id

    def __save_to_characteristic_table(self, characteristic_element, service_id):
        # type: (ET, int) -> int
        type = characteristic_element.attrib['type']
        requirement = characteristic_element[0].text.strip()
        characteristic = Characteristic(type, requirement, service_id)
        characteristic_controller.create(characteristic)
        return characteristic.id
