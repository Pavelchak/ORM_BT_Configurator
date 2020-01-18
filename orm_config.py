import os


class OrmConfig:
    DB_FILE = 'cy_xml_db.sqlite'
    DB_PATH = ''
    IS_DEL_DB_FILE = True
    DB_CONNECT_STR = 'sqlite:///' + DB_PATH + DB_FILE
    # DB_CONNECT_STR = 'sqlite:///:memory:'
    ECHO = False
    LOAD_DATA_TO_DB = False

    # Paths to xml files
    __local_path = os.path.dirname(__file__)
    GATT_PROFILE_PATH = os.path.abspath(os.path.join(__local_path, "resources/psoc6_gatt/Profiles"))
    GATT_SERVICES_PATH = os.path.abspath(os.path.join(__local_path, "resources/psoc6_gatt/Services"))
    GATT_CHARACTERISTICS_PATH = os.path.abspath(os.path.join(__local_path, "resources/psoc6_gatt/Characteristics"))
    GATT_DESCRIPTOR_PATH = os.path.abspath(os.path.join(__local_path, "resources/psoc6_gatt/Descriptors"))

    PSOC6_COMPONENT_PATH = os.path.abspath(os.path.join(__local_path, "resources/bt_cnf_psoc6_object_snapshot.xml"))
