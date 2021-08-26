from sqlalchemy.orm import Session

from db.Exceptions import ValidDataException
from db.Models import Jockeys


def create_jockey(session: Session, body: dict) -> Jockeys:
    if int(body["rating"]) > 10:
        raise ValidDataException

    try:
        new_jockeys = Jockeys(
            FirstName=body["FirstName"],
            LastName=body["LastName"],
            Patronymic=body["Patronymic"],
            Age=body["Age"],
            PhoneNumber=body["PhoneNumber"],
            rating=body["rating"]

        )
        session.add(new_jockeys)
    except:
        raise ValidDataException
    return new_jockeys
