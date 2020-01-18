from collections import OrderedDict
from orm_config import OrmConfig as Cfg
from ulit.psoc6_gatt_db_loader.component_loader import FormComponentDbLoader
from controller.mapped_qt_components import component_controller
from domain.mapped_qt_components import Component


class MyView:
    def __init__(self):
        self.__menu = OrderedDict()

        self.__menu["A"] = "  A - Load components-XML to DB"

        self.__menu["1"] = "  1 - Table Component"
        self.__menu["11"] = "  11 - Select Component"
        self.__menu["12"] = "  12 - Find by ID Component"
        self.__menu["13"] = "  13 - Create Component"
        self.__menu["14"] = "  14 - Update Component"
        self.__menu["15"] = "  15 - Patch Component"
        self.__menu["16"] = "  16 - Delete Component"

        self.__menu["Q"] = "  Q - exit"

        self.__menu_methods = dict()

        self.__menu_methods["A"] = self.__load_component_xml_to_db

        self.__menu_methods["11"] = self.__select_component
        self.__menu_methods["12"] = self.__find_by_id_component
        self.__menu_methods["13"] = self.__create_component
        self.__menu_methods["14"] = self.__update_component
        self.__menu_methods["15"] = self.__patch_component
        self.__menu_methods["16"] = self.__delete_component

    def __load_component_xml_to_db(self):
        FormComponentDbLoader(Cfg.PSOC6_COMPONENT_PATH).load_to_db_from_xml()

    # ---------------------------------------------------

    def __select_component(self):
        print "TABLE Component:"
        components = component_controller.find_all()
        for component in components:
            print component

    def __create_component(self):
        element_id = raw_input("Input Component->element_id:")
        component_class = raw_input("Input Component->component_class:")
        container = raw_input("Input Component->container:")
        text = raw_input("Input Component->text:")
        name = raw_input("Input Component->name:")
        title = raw_input("Input Component->title:")
        component_id = int(raw_input("Input Component->component_id:"))
        component = Component(element_id, component_class, container, text, name, title, component_id)
        component_controller.create(component)
        print component.id

    def __update_component(self):
        key = int(raw_input("Input Component->ID:"))
        element_id = raw_input("Input Component->element_id:")
        component_class = raw_input("Input Component->component_class:")
        container = raw_input("Input Component->container:")
        text = raw_input("Input Component->text:")
        name = raw_input("Input Component->name:")
        title = raw_input("Input Component->title:")
        component_id = int(raw_input("Input Component->component_id:"))
        component = Component(element_id, component_class, container, text, name, title, component_id)
        component_controller.update(key, component)

    def __delete_component(self):
        key = int(raw_input("Input Component->ID:"))
        component_controller.delete(key)

    def __find_by_id_component(self):
        key = int(raw_input("Input Component->ID:"))
        component = component_controller.find_by_id(key)
        print component
        for child in component.child_components:
            print "   " + str(child)

    def __patch_component(self):
        key = int(raw_input("Input Component->ID:"))
        field_name = raw_input("Input Component->field name:")
        value = raw_input("Input Component->new VALUE:")
        component_controller.patch(key, field_name, value)

    # ---------------------------------------------------

    def output_menu(self):
        print "MENU:"
        for key in self.__menu.keys():
            if len(key) == 1:
                print self.__menu.get(key)

    def output_sub_menu(self, fig):
        print "SubMENU:"
        for key in self.__menu.keys():
            if len(key) != 1 and key[0] == fig:
                print self.__menu.get(key)

    def show(self):
        key_menu = ""
        while key_menu != "Q":
            self.output_menu()
            key_menu = str(raw_input()).upper()

            if key_menu.isdigit():
                self.output_sub_menu(key_menu)
                print "Please, select menu point."
                key_menu = str(raw_input()).upper()
            if key_menu in self.__menu_methods:
                self.__menu_methods[key_menu]()
