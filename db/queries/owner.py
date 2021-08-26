from sqlalchemy.orm import Session

from db.Exceptions import ValidDataException
from db.Models import Owners


def create_owner(session: Session, body: dict) -> Owners:
    try:
        new_owner = Owners(

            FirstName=body["FirstName"],
            LastName=body["LastName"],
            Patronymic=body["Patronymic"],
            Age=body["Age"],
            PhoneNumber=body["PhoneNumber"]

        )
        session.add(new_owner)
    except:
        raise ValidDataException
    return new_owner
