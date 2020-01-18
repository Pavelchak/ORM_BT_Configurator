from abc import abstractmethod
from orm_config import OrmConfig as Cnf
import os
from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


class IGeneral():
    @abstractmethod
    def full_update(self, obj):
        pass


if Cnf.IS_DEL_DB_FILE and os.path.exists(Cnf.DB_FILE):
    os.remove(Cnf.DB_FILE)
engine = create_engine(Cnf.DB_CONNECT_STR, echo=Cnf.ECHO)
Session = sessionmaker(bind=engine)
Base = declarative_base()


@event.listens_for(engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()
