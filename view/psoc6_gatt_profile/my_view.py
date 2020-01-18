from collections import OrderedDict
from controller.psoc6_gatt_profile import characteristic_controller, client_controller, gap_role_controller, \
    profile_controller, role_controller, service_controller
from domain.psoc6_gatt_profile import Characteristic, Client, GapRole, Profile, Role, Service
import initial_data as in_data
from orm_config import OrmConfig as Cfg
from ulit.psoc6_gatt_db_loader.component_loader import FormComponentDbLoader
from ulit.psoc6_gatt_db_loader.profile_loader import GattDbLoader


class MyView:
    def __init__(self):
        if Cfg.LOAD_DATA_TO_DB:
            in_data.load_data_to_db()
        self.__menu = OrderedDict()

        self.__menu["A"] = "  A - Load PROFILE XML to DB"
        self.__menu["B"] = "  B - Load component XML to DB"

        self.__menu["1"] = "  1 - Table Profile"
        self.__menu["11"] = "  11 - Select Profile"
        self.__menu["12"] = "  12 - Find by ID Profile"
        self.__menu["13"] = "  13 - Create Profile"
        self.__menu["14"] = "  14 - Update Profile"
        self.__menu["15"] = "  15 - Patch Profile"
        self.__menu["16"] = "  16 - Delete Profile"

        self.__menu["2"] = "  2 - Table Role"
        self.__menu["21"] = "  21 - Select Role"
        self.__menu["22"] = "  22 - Find by ID Role"
        self.__menu["23"] = "  23 - Create Role"
        self.__menu["24"] = "  24 - Update Role"
        self.__menu["25"] = "  25 - Patch Role"
        self.__menu["26"] = "  26 - Delete Role"

        self.__menu["3"] = "  3 - Table Gap_Role"
        self.__menu["31"] = "  31 - Select Gap_Role"
        self.__menu["32"] = "  32 - Find by ID Gap_Role"
        self.__menu["33"] = "  33 - Create Gap_Role"
        self.__menu["34"] = "  34 - Update Gap_Role"
        self.__menu["35"] = "  35 - Patch Gap_Role"
        self.__menu["36"] = "  36 - Delete Gap_Role"

        self.__menu["4"] = "  4 - Table Client"
        self.__menu["41"] = "  41 - Select Client"
        self.__menu["42"] = "  42 - Find by ID Client"
        self.__menu["43"] = "  43 - Create Client"
        self.__menu["44"] = "  44 - Update Client"
        self.__menu["45"] = "  45 - Patch Client"
        self.__menu["46"] = "  46 - Delete Client"

        self.__menu["5"] = "  5 - Table Service"
        self.__menu["51"] = "  51 - Select Service"
        self.__menu["52"] = "  52 - Find by ID Service"
        self.__menu["53"] = "  53 - Create Service"
        self.__menu["54"] = "  54 - Update Service"
        self.__menu["55"] = "  55 - Patch Service"
        self.__menu["56"] = "  56 - Delete Service"

        self.__menu["6"] = "  6 - Table Characteristic"
        self.__menu["61"] = "  61 - Select Characteristic"
        self.__menu["62"] = "  62 - Find by ID Characteristic"
        self.__menu["63"] = "  63 - Create Characteristic"
        self.__menu["64"] = "  64 - Update Characteristic"
        self.__menu["65"] = "  65 - Patch Characteristic"
        self.__menu["66"] = "  66 - Delete Characteristic"

        self.__menu["Q"] = "  Q - exit"

        self.__menu_methods = dict()

        self.__menu_methods["A"] = self.__load_profile_xml_to_db
        self.__menu_methods["B"] = self.__load_component_xml_to_db

        self.__menu_methods["11"] = self.__select_profile
        self.__menu_methods["12"] = self.__find_by_id_profile
        self.__menu_methods["13"] = self.__create_profile
        self.__menu_methods["14"] = self.__update_profile
        self.__menu_methods["15"] = self.__patch_profile
        self.__menu_methods["16"] = self.__delete_profile

        self.__menu_methods["21"] = self.__select_role
        self.__menu_methods["22"] = self.__find_by_id_role
        self.__menu_methods["23"] = self.__create_role
        self.__menu_methods["24"] = self.__update_role
        self.__menu_methods["25"] = self.__patch_role
        self.__menu_methods["26"] = self.__delete_role

        self.__menu_methods["31"] = self.__select_gap_role
        self.__menu_methods["32"] = self.__find_by_id_gap_role
        self.__menu_methods["33"] = self.__create_gap_role
        self.__menu_methods["34"] = self.__update_gap_role
        self.__menu_methods["35"] = self.__patch_gap_role
        self.__menu_methods["36"] = self.__delete_gap_role

        self.__menu_methods["41"] = self.__select_client
        self.__menu_methods["42"] = self.__find_by_id_client
        self.__menu_methods["43"] = self.__create_client
        self.__menu_methods["44"] = self.__update_client
        self.__menu_methods["45"] = self.__patch_client
        self.__menu_methods["46"] = self.__delete_client

        self.__menu_methods["51"] = self.__select_service
        self.__menu_methods["52"] = self.__find_by_id_service
        self.__menu_methods["53"] = self.__create_service
        self.__menu_methods["54"] = self.__update_service
        self.__menu_methods["55"] = self.__patch_service
        self.__menu_methods["56"] = self.__delete_service
        #
        self.__menu_methods["61"] = self.__select_characteristic
        self.__menu_methods["62"] = self.__find_by_id_characteristic
        self.__menu_methods["63"] = self.__create_characteristic
        self.__menu_methods["64"] = self.__update_characteristic
        self.__menu_methods["65"] = self.__patch_characteristic
        self.__menu_methods["66"] = self.__delete_characteristic

    def __load_profile_xml_to_db(self):
        print "clear all tables..."
        characteristic_controller.delete_all()
        service_controller.delete_all()
        client_controller.delete_all()
        gap_role_controller.delete_all()
        role_controller.delete_all()
        profile_controller.delete_all()
        print "loading..."
        GattDbLoader(Cfg.GATT_PROFILE_PATH).load_to_db_from_xml()

    def __load_component_xml_to_db(self):
        FormComponentDbLoader(Cfg.PSOC6_COMPONENT_PATH).load_to_db_from_xml()

    # ---------------------------------------------------

    def __select_profile(self):
        print "TABLE Profile:"
        profiles = profile_controller.find_all()
        for profile in profiles:
            print profile

    def __create_profile(self):
        type = raw_input("Input Profile->Type:")
        name = raw_input("Input Profile->Name:")
        abstract = raw_input("Input Profile->Abstract:")
        summary = raw_input("Input Profile->Summary:")
        profile = Profile(type, name, abstract, summary)
        profile_controller.create(profile)
        print profile.id

    def __update_profile(self):
        key = int(raw_input("Input Profile->ID:"))
        type = raw_input("Input Profile->new Type:")
        name = raw_input("Input Profile->new Name:")
        abstract = raw_input("Input Profile->new Abstract:")
        summary = raw_input("Input Profile->new Summary:")
        profile = Profile(type, name, abstract, summary)
        profile_controller.update(key, profile)

    def __delete_profile(self):
        key = int(raw_input("Input Profile->ID:"))
        profile_controller.delete(key)

    def __find_by_id_profile(self):
        key = int(raw_input("Input Profile->ID:"))
        profile = profile_controller.find_by_id(key)
        print profile
        for role in profile.roles:
            print role

    def __patch_profile(self):
        key = int(raw_input("Input Profile->ID:"))
        field_name = raw_input("Input Profile->field name:")
        value = raw_input("Input Profile->new VALUE:")
        profile_controller.patch(key, field_name, value)

    # ---------------------------------------------------

    def __select_role(self):
        print "TABLE Role:"
        roles = role_controller.find_all()
        for role in roles:
            print role

    def __create_role(self):
        name = raw_input("Input Role->Name:")
        prof_profile_id = int(raw_input("Input Role->prof_profile_id:"))
        role = Role(name, prof_profile_id)
        role_controller.create(role)
        print role.id

    def __update_role(self):
        key = int(raw_input("Input Role->ID:"))
        name = raw_input("Input Role->new Name:")
        prof_profile_id = int(raw_input("Input Role->prof_profile_id:"))
        role = Role(name, prof_profile_id)
        role_controller.update(key, role)

    def __delete_role(self):
        key = int(raw_input("Input Role->ID:"))
        role_controller.delete(key)

    def __find_by_id_role(self):
        key = int(raw_input("Input Role->ID:"))
        role = role_controller.find_by_id(key)
        print role
        for gap_role in role.gap_roles:
            print gap_role
        for client in role.clients:
            print client
        for service in role.services:
            print service

    def __patch_role(self):
        key = int(raw_input("Input Role->ID:"))
        field_name = raw_input("Input Role->field name:")
        value = raw_input("Input Role->new VALUE:")
        role_controller.patch(key, field_name, value)

    # ---------------------------------------------------

    def __select_gap_role(self):
        print "TABLE GapRole:"
        gap_roles = gap_role_controller.find_all()
        for gap_role in gap_roles:
            print gap_role

    def __create_gap_role(self):
        gap_role = raw_input("Input GapRole->gap_role:")
        prof_role_id = int(raw_input("Input GapRole->prof_profile_id:"))
        gap_role = GapRole(gap_role, prof_role_id)
        gap_role_controller.create(gap_role)
        print gap_role.id

    def __update_gap_role(self):
        key = int(raw_input("Input GapRole->ID:"))
        gap_role = raw_input("Input GapRole->gap_role:")
        prof_role_id = int(raw_input("Input GapRole->prof_profile_id:"))
        gap_role = GapRole(gap_role, prof_role_id)
        gap_role_controller.update(key, gap_role)

    def __delete_gap_role(self):
        key = int(raw_input("Input GapRole->ID:"))
        gap_role_controller.delete(key)

    def __find_by_id_gap_role(self):
        key = int(raw_input("Input GapRole->ID:"))
        gap_role = gap_role_controller.find_by_id(key)
        print gap_role

    def __patch_gap_role(self):
        key = int(raw_input("Input GapRole->ID:"))
        field_name = raw_input("Input GapRole->field name:")
        value = raw_input("Input GapRole->new VALUE:")
        gap_role_controller.patch(key, field_name, value)

    # ---------------------------------------------------

    def __select_client(self):
        print "TABLE Client:"
        clients = client_controller.find_all()
        for client in clients:
            print client

    def __create_client(self):
        type = raw_input("Input Client->Type:")
        requirement = raw_input("Input Client->Requirement:")
        prof_role_id = int(raw_input("Input Client->prof_profile_id:"))
        client = Client(type, requirement, prof_role_id)
        client_controller.create(client)
        print client.id

    def __update_client(self):
        key = int(raw_input("Input Client->ID:"))
        type = raw_input("Input Client->Type:")
        requirement = raw_input("Input Client->Requirement:")
        prof_role_id = int(raw_input("Input Client->prof_profile_id:"))
        client = Client(type, requirement, prof_role_id)
        client_controller.update(key, client)

    def __delete_client(self):
        key = int(raw_input("Input Client->ID:"))
        client_controller.delete(key)

    def __find_by_id_client(self):
        key = int(raw_input("Input Client->ID:"))
        client = client_controller.find_by_id(key)
        print client

    def __patch_client(self):
        key = int(raw_input("Input Client->ID:"))
        field_name = raw_input("Input Client->field name:")
        value = raw_input("Input Client->new VALUE:")
        client_controller.patch(key, field_name, value)

    # ---------------------------------------------------

    def __select_service(self):
        print "TABLE Service:"
        clients = service_controller.find_all()
        for client in clients:
            print client

    def __create_service(self):
        type = raw_input("Input Service->Type:")
        declaration = raw_input("Input Service->declaration:")
        requirement = raw_input("Input Service->Requirement:")
        prof_role_id = int(raw_input("Input Service->prof_profile_id:"))
        service = Service(type, declaration, requirement, prof_role_id)
        service_controller.create(service)
        print service_controller.id

    def __update_service(self):
        key = int(raw_input("Input Service->ID:"))
        type = raw_input("Input Service->Type:")
        declaration = raw_input("Input Service->declaration:")
        requirement = raw_input("Input Service->Requirement:")
        prof_role_id = int(raw_input("Input Service->prof_profile_id:"))
        service = Service(type, declaration, requirement, prof_role_id)
        service_controller.update(key, service)

    def __delete_service(self):
        key = int(raw_input("Input Service->ID:"))
        service_controller.delete(key)

    def __find_by_id_service(self):
        key = int(raw_input("Input Service->ID:"))
        service = service_controller.find_by_id(key)
        print service
        for characteristic in service.characteristics:
            print characteristic

    def __patch_service(self):
        key = int(raw_input("Input Service->ID:"))
        field_name = raw_input("Input Service->field name:")
        value = raw_input("Input Service->new VALUE:")
        service_controller.patch(key, field_name, value)

    # ---------------------------------------------------

    def __select_characteristic(self):
        print "TABLE Characteristic:"
        characteristics = characteristic_controller.find_all()
        for characteristic in characteristics:
            print characteristic

    def __create_characteristic(self):
        type = raw_input("Input Characteristic->Type:")
        requirement = raw_input("Input Characteristic->Requirement:")
        prof_service_id = int(raw_input("Input Characteristic->prof_profile_id:"))
        characteristic = Characteristic(type, requirement, prof_service_id)
        characteristic_controller.create(characteristic)
        print characteristic.id

    def __update_characteristic(self):
        key = int(raw_input("Input Characteristic->ID:"))
        type = raw_input("Input Characteristic->Type:")
        requirement = raw_input("Input Characteristic->Requirement:")
        prof_service_id = int(raw_input("Input Characteristic->prof_profile_id:"))
        characteristic = Characteristic(type, requirement, prof_service_id)
        characteristic_controller.update(key, characteristic)

    def __delete_characteristic(self):
        key = int(raw_input("Input Characteristic->ID:"))
        characteristic_controller.delete(key)

    def __find_by_id_characteristic(self):
        key = int(raw_input("Input Characteristic->ID:"))
        characteristic = characteristic_controller.find_by_id(key)
        print characteristic

    def __patch_characteristic(self):
        key = int(raw_input("Input Characteristic->ID:"))
        field_name = raw_input("Input Characteristic->field name:")
        value = raw_input("Input Characteristic->new VALUE:")
        characteristic_controller.patch(key, field_name, value)

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
