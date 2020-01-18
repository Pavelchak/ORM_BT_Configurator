from base import Session, engine, Base
from psoc6_gatt_profile import Characteristic, Client, GapRole, Profile, Role, Service
from mapped_qt_components import Component


Base.metadata.create_all(engine)
session = Session()
