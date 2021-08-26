import sqlalchemy
from sqlalchemy.engine import Engine
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import sessionmaker, Session

from db.Exceptions import ConnectionException, DBnotFindException


class DataBase:
    connection: Engine
    session_factory: sessionmaker
    _test_query = 'SELECT 1'

    def __init__(self, connection: Engine):
        self.connection = connection
        self.session_factory = sessionmaker(bind=self.connection)

    def check_connection(self):
        try:
            self.connection.execute(self._test_query).fetchone()
        except OperationalError:
            raise DBnotFindException
        except:
            raise ConnectionException

    def make_session(self) -> Session:
        try:
            return Session(bind=self.connection)
        except:
            raise ConnectionException
