from sqlalchemy.orm import Session

from db.Exceptions import ValidDataException
from db.Models import Horses


def create_horse(session: Session, body: dict) -> Horses:
    try:
        new_horse = Horses(

            Nickname=body["Nickname"],
            Gender=body["Gender"],
            DateOfBirth=body["DateOfBirth"],
            OwnerId=body["OwnerId"],

        )

        session.add(new_horse)
    except:
        raise ValidDataException
    return new_horse
