from sqlalchemy.orm import Session

from db.Exceptions import ValidDataException
from db.Models import Matches_results


def create_match_result(session: Session, body: dict) -> Matches_results:
    try:
        new_match_results = Matches_results(
            match_id=body["match_id"],
            firstPlace_jockey=body["firstPlace_jockey"],
            SecondPlace_jockey=body["SecondPlace_jockey"],
            ThirdPlace_jockey=body["ThirdPlace_jockey"],
            firstPlace_horse=body["firstPlace_horse"],
            SecondPlace_horse=body["SecondPlace_horse"],
            ThirdPlace_horse=body["ThirdPlace_horse"]

        )
        session.add(new_match_results)
    except:
        raise ValidDataException
    return new_match_results
