from models.base import Base, intpk, employer_id, str_80
from sqlalchemy.orm import Mapped
from typing import Optional
from settings.basic import sql_engine


class Employer(Base):
    __tablename__ = 'employers'
    employer_id: Mapped[intpk]
    name: Mapped[str_80]


class Vacancy(Base):
    __tablename__ = 'vacancies'
    vacancy_id: Mapped[intpk]
    employer_id: Mapped[employer_id]
    name: Mapped[str]
    salary: Mapped[Optional[int]]
    requirements: Mapped[Optional[str]]


Base.metadata.create_all(sql_engine)
