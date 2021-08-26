from sqlalchemy.orm import Session

import db
from db.Exceptions import ValidDataException
from db.Models import Jockeys


def up_data(ses: Session, table: db.Models, idu: int, colum: str, value):
    obj = ses.query(table).filter(table.id == idu).first()

    if hasattr(obj, colum):
        setattr(obj, colum, value)
        ses.add(obj)
        ses.commit()
    else:
        raise ValidDataException
