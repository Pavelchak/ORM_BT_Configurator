from datetime import datetime

from controller.psoc6_gatt_profile import characteristic_controller, client_controller, gap_role_controller, \
    profile_controller, \
    role_controller, service_controller
from domain.psoc6_gatt_profile import Characteristic, Client, GapRole, Profile, Role, Service


def to_date(str):
    return datetime.strptime(str, "%d-%m-%Y").date()


def load_data_to_db():
    profile = Profile("org.bluetooth.psoc6_gatt_profile.cycling_speed_and_cadence", "Cycling Speed and Cadence", "None", "None")
    profile_controller.create(profile)

    profile = Profile("org.bluetooth.psoc6_gatt_profile.heart_rate", "Heart Rate", "None", "None")
    profile_controller.create(profile)

    profile = Profile("org.bluetooth.psoc6_gatt_profile.proximity", "Proximity", "None", "None")
    profile_controller.create(profile)

    profile = Profile("org.bluetooth.psoc6_gatt_profile.proximity", "Proximity", "None",
                      "The Heart Rate Profile is used to enable a data collection device to obtain data from a Heart Rate Sensor that exposes the Heart Rate Service.\n" \
                       "The Heart Rate Profile is used to enable a data collection device to obtain data from a Heart Rate Sensor that exposes the Heart Rate Service.\n" \
                      "The Heart Rate Profile is used to enable a data collection device to obtain data from a Heart Rate Sensor that exposes the Heart Rate Service.")
    profile_controller.create(profile)

    # --------------------------------------------------------------

    role = Role("CSC Sensor", 1)
    role_controller.create(role)

    role = Role("Collector", 1)
    role_controller.create(role)

    role = Role("Heart Rate Sensor", 2)
    role_controller.create(role)

    role = Role("Collector", 2)
    role_controller.create(role)

    # --------------------------------------------------------------

    gap_role = GapRole("Peripheral", 1)
    gap_role_controller.create(gap_role)

    gap_role = GapRole("Central", 2)
    gap_role_controller.create(gap_role)

    gap_role = GapRole("Peripheral", 3)
    gap_role_controller.create(gap_role)

    gap_role = GapRole("Central", 4)
    gap_role_controller.create(gap_role)

    # --------------------------------------------------------------

    client = Client("org.bluetooth.service.cycling_speed_and_cadence", "Mandatory", 2)
    client_controller.create(client)

    client = Client("org.bluetooth.service.device_information", "Optional", 2)
    client_controller.create(client)

    client = Client("org.bluetooth.service.heart_rate", "Mandatory", 4)
    client_controller.create(client)

    client = Client("org.bluetooth.service.device_information", "Optional", 4)
    client_controller.create(client)

    # --------------------------------------------------------------

    service = Service("org.bluetooth.service.cycling_speed_and_cadence", "PrimarySingleInstance", "Mandatory", 1)
    service_controller.create(service)

    service = Service("org.bluetooth.service.device_information", "Primary", "Optional", 1)
    service_controller.create(service)

    service = Service("org.bluetooth.service.heart_rate", "Primary", "Mandatory", 3)
    service_controller.create(service)

    service = Service("org.bluetooth.service.device_information", "PrimarySingleInstance", "Mandatory", 3)
    service_controller.create(service)

    # --------------------------------------------------------------

    characteristic = Characteristic("org.bluetooth.characteristic.manufacturer_name_string", "Optional", 2)
    characteristic_controller.create(characteristic)

    characteristic = Characteristic("org.bluetooth.characteristic.model_number_string", "Optional", 2)
    characteristic_controller.create(characteristic)

    characteristic = Characteristic("org.bluetooth.characteristic.manufacturer_name_string", "Mandatory", 4)
    characteristic_controller.create(characteristic)
