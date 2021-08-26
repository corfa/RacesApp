from sqlalchemy import create_engine

from ConfigApp import ConfigApp
from app import RacesApp
from db.DataBase import DataBase
from db.Exceptions import DBnotFindException
from newDB import CreateDataBase
from say.bayHorse import SayBay
from say.helloHorse import SayHello

config = ConfigApp()

engine = create_engine(
    config.url,
)

db = DataBase(engine)
try:
    db.check_connection()

except DBnotFindException:
    CreateDataBase(config)

app = RacesApp(db)
app.geometry(config.WindowSize)
SayHello()
app.mainloop()
SayBay()

