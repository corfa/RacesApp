from sqlalchemy.orm import Session

from db.Exceptions import ValidDataException
from db.Models import Matches


def create_match(session: Session, body: dict) -> Matches:
    try:
        new_match = Matches(
            name=body["name"],
            hippodrome=body["place"],
            date=body["date"]
        )
        session.add(new_match)
    except:
        raise ValidDataException
    return new_match
