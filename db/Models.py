from sqlalchemy import Column, Integer, create_engine, String, ForeignKey, Date, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True

    id = Column(
        Integer,
        nullable=False,
        unique=True,
        primary_key=True,
        autoincrement=True,
    )

    def __repr__(self):
        return f'{self.__class__.__name__}'


class Owners(BaseModel):
    __tablename__ = 'owners'

    FirstName = Column(String(100), nullable=False)
    LastName = Column(String(100), nullable=False)
    Patronymic = Column(String(200), nullable=False)
    Age = Column(Integer, nullable=False)
    PhoneNumber = Column(String(13), nullable=False, unique=True)


class Horses(BaseModel):
    __tablename__ = 'horses'
    Nickname = Column(String(100), nullable=False)
    Gender = Column(String(3), nullable=False)
    DateOfBirth = Column(Date, nullable=False)
    OwnerId = Column(Integer, ForeignKey('owners.id'),nullable=False)


class Jockeys(BaseModel):
    __tablename__ = 'jockeys'
    FirstName = Column(String(100), nullable=False)
    LastName = Column(String(100), nullable=False)
    Patronymic = Column(String(200), nullable=False)
    Age = Column(Integer, nullable=False)
    PhoneNumber = Column(String(13), nullable=False, unique=True)
    rating = Column(Float, nullable=False)


class Matches(BaseModel):
    __tablename__ = 'matches'
    name = Column(String(100), nullable=False)
    hippodrome = Column(String(100), nullable=False)
    date = Column(Date, nullable=False)


class Matches_results(BaseModel):
    __tablename__ = 'matches_results'
    match_id = Column(Integer, ForeignKey('matches.id'), nullable=False, unique=True)
    firstPlace_jockey = Column(Integer, ForeignKey('jockeys.id'), nullable=False)
    SecondPlace_jockey = Column(Integer, ForeignKey('jockeys.id'), nullable=False)
    ThirdPlace_jockey = Column(Integer, ForeignKey('jockeys.id'), nullable=False)
    firstPlace_horse = Column(Integer, ForeignKey('horses.id'), nullable=False)
    SecondPlace_horse = Column(Integer, ForeignKey('horses.id'), nullable=False)
    ThirdPlace_horse = Column(Integer, ForeignKey('horses.id'), nullable=False)
