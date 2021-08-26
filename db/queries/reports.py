from datetime import datetime
from typing import List

from sqlalchemy.orm import Session

from db.Models import Owners, Horses, Jockeys, Matches, Matches_results


def report_for_owners(session: Session) -> List[Owners]:
    ownersId = session.execute("""SELECT OwnerId AS ln
     FROM
         (SELECT OwnerId, count(*) as Counter
          FROM `horses`
          GROUP BY `OwnerId`) AS tbl WHERE Counter > 2;""")

    mass = []

    for i in ownersId:
        mass.append(i[0])

    mass_owners = []

    for i in mass:
        owner = session.query(Owners).filter(Owners.id == i).first()

        mass_owners.append(owner)
    return mass_owners


def report_for_jockeys(session: Session, rating: float) -> List[Jockeys]:
    jockeys = session.query(Jockeys).filter(Jockeys.rating >= rating).all()
    return jockeys


def report_for_horses(session: Session, dateOne: str, dateTo: str) -> List:
    end = []

    matches = session.query(Matches).filter(Matches.date.between(dateOne, dateTo))
    mass_matches = []
    for i in matches:
        mass_matches.append(i)

    for i in mass_matches:
        result = {"MatchName": None, "Place": None, "Date": None,
                  "First_horse": {"NickName": None, "Gender": None, "Place": 'One',
                                  "DateOfBrinth": None, "OwnerId": None},
                  "Second_Horse": {"NickName": None, "Gender": None, "Place": 'To',
                                   "DateOfBrinth": None, "OwnerId": None}}
        results_math = session.query(Matches_results).filter(Matches_results.match_id == i.id).first()

        if results_math is not None:
            result["MatchName"] = i.name
            result["Place"] = i.hippodrome
            result["Date"] = i.date.strftime("%Y-%m-%d")
            first_hors = session.query(Horses).filter(Horses.id == results_math.firstPlace_horse).first()
            result["First_horse"]["NickName"] = first_hors.Nickname
            result["First_horse"]["Gender"] = first_hors.Gender
            result["First_horse"]["OwnerId"] = first_hors.OwnerId
            result["First_horse"]["DateOfBrinth"] = first_hors.DateOfBirth.strftime("%Y-%m-%d")
            second_hors = session.query(Horses).filter(Horses.id == results_math.SecondPlace_horse).first()
            result["Second_Horse"]["NickName"] = second_hors.Nickname
            result["Second_Horse"]["Gender"] = second_hors.Gender
            result["Second_Horse"]["OwnerId"] = second_hors.OwnerId
            result["Second_Horse"]["DateOfBrinth"] = second_hors.DateOfBirth.strftime("%Y-%m-%d")

            end.append(result)

    return end


def report_for_ipadrom(session: Session, ipadrom: str)-> List:
    end = []
    MounthAgo = None
    currentMonth = datetime.now().month
    currentYear = datetime.now().year
    if currentMonth == 12:
        MounthAgo = 1
    else:
        MounthAgo = currentMonth - 1
    secondDate = str(currentYear) + "." + str(MounthAgo) + "." + "30"

    firstDate = str(currentYear) + "." + str(MounthAgo) + "." + "1"
    mathes = session.query(Matches).filter(Matches.date.between(firstDate, secondDate), Matches.hippodrome == ipadrom).all()
    for i in mathes:

        res = session.query(Matches_results).filter(Matches_results.match_id == i.id).first()
        if res is not None:
            FirstJockey = session.query(Jockeys).filter(Jockeys.id == res.firstPlace_jockey).first()

            SecondJockey = session.query(Jockeys).filter(Jockeys.id == res.SecondPlace_jockey).first()

            ThirdJockey = session.query(Jockeys).filter(Jockeys.id == res.ThirdPlace_jockey).first()
            end.append(SecondJockey)
            end.append(FirstJockey)
            end.append(ThirdJockey)

    res = []

    for i in end:
        if i.id not in res:
            res.append(i)

    return res
