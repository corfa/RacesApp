import pymysql
from sqlalchemy import create_engine

from ConfigApp import ConfigApp
from db import Models


def CreateDataBase(Config: ConfigApp):
    print("The database was not found. Trying to create a new one")
    connection = pymysql.connections.Connection(user=Config.user, password=Config.dbPassword, host=Config.dbHost,
                                                port=3306,
                                                cursorclass=pymysql.cursors.DictCursor)
    with connection:
        with connection.cursor() as cursor:
            sql = rf'CREATE DATABASE {Config.dbName}'
            cursor.execute(sql)
        connection.commit()

    engine = create_engine(
        Config.url,
    )
    Models.Base.metadata.create_all(engine)
    print("a new database was created")
