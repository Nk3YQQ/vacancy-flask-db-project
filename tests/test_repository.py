import pytest
from sqlalchemy.orm import sessionmaker

from models import Employer, Vacancy
from repository import EmployerRepository, VacancyRepository
from settings.basic import sql_engine

session = sessionmaker(sql_engine)

employers_repo = EmployerRepository(session, Employer)
vacancy_repo = VacancyRepository(session, Vacancy)


@pytest.fixture
def employer() -> Employer:
    return Employer(employer_id=1, employer_name="Компания N")


@pytest.fixture
def vacancy() -> Vacancy:
    return Vacancy(
        vacancy_id=1,
        employer_id=1,
        vacancy_name="Python Developer",
        salary=150000,
        requirements="Python, PostgreSQL, Git",
    )


def test_employer_save(employer: Employer) -> None:
    employers_repo.save(employer)


def test_vacancy_save(vacancy: Vacancy) -> None:
    vacancy_repo.save(vacancy)


def test_employer_find(employer: Employer) -> None:
    assert employers_repo.find(employer) is True


def test_vacancy_find(vacancy: Vacancy) -> None:
    assert vacancy_repo.find(vacancy) is True


def test_vacancy_delete(vacancy: Vacancy) -> None:
    vacancy_repo.delete(vacancy)


def test_vacancy_not_find(vacancy: Vacancy) -> None:
    assert vacancy_repo.find(vacancy) is not True


def test_employer_delete(employer: Employer) -> None:
    employers_repo.delete(employer)


def test_employer_not_find(employer: Employer) -> None:
    assert employers_repo.find(employer) is not True


def test_employer_content() -> None:
    content = employers_repo.content()
    assert isinstance(content, list)


def test_vacancy_content() -> None:
    content = vacancy_repo.content()
    assert isinstance(content, list)
