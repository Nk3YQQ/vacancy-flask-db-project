from models.base import Base, intpk, employer_id, str_40, str_80
from sqlalchemy.orm import Mapped
from typing import Optional


class Employer(Base):
    __tablename__ = 'employees'
    employer_id: Mapped[intpk]
    name: Mapped[str_80]


class Vacancy(Base):
    __tablename__ = 'vacancies'
    vacancy_id: Mapped[intpk]
    employer_id: Mapped[employer_id]
    name: Mapped[str_40]
    salary: Mapped[Optional[int]]
    description: Mapped[Optional[str]]
    requirements: Mapped[Optional[str]]
