from sqlalchemy.orm import sessionmaker

from dbmanager import DBManager
from models import Employer, Vacancy
from settings.basic import sql_engine

session = sessionmaker(sql_engine)

db_manager = DBManager(session, Employer, Vacancy)


def test_get_all_vacancies() -> None:
    all_vacancies = db_manager.get_all_vacancies()
    assert isinstance(all_vacancies, list)
    for vacancy in all_vacancies:
        assert isinstance(vacancy, dict)


def test_get_companies_and_vacancies_count() -> None:
    companies = db_manager.get_companies_and_vacancies_count()
    assert isinstance(companies, list)
    for company in companies:
        assert isinstance(company, dict)


def test_avg_salary() -> None:
    avg_salary = db_manager.get_avg_salary()
    assert isinstance(avg_salary, int)


def test_get_vacancies_with_higher_salary() -> None:
    vacancies_with_higher_salary = db_manager.get_vacancies_with_higher_salary()
    assert isinstance(vacancies_with_higher_salary, list)
    for vacancy in vacancies_with_higher_salary:
        assert isinstance(vacancy, dict)


def test_get_vacancies_with_keyword():
    keyword = "Python"
    vacancies_with_keyword = db_manager.get_vacancies_with_keyword(keyword)
    assert isinstance(vacancies_with_keyword, list)
    for vacancy in vacancies_with_keyword:
        assert keyword in vacancy["vacancy_name"] or keyword in vacancy["requirements"]
        assert isinstance(vacancy, dict)
