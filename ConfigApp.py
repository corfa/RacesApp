import os

from dotenv import load_dotenv

load_dotenv()


class ConfigApp:
    user = os.getenv("MySQLUser", "root")
    dbPassword = os.getenv("MySQLPassword", "00000")
    dbName = os.getenv("MySQLDB", "user")
    dbHost = os.getenv("host", "localhost")
    port = os.getenv("port", "4000")
    url = rf'mysql+pymysql://{user}:{dbPassword}@{dbHost}:{port}/{dbName}'

    WindowSize = os.getenv("WindowSize", "400x400")
