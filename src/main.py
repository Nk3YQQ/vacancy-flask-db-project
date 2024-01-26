from flask import Flask
from sqlalchemy.orm import sessionmaker

from dbmanager import DBManager
from dbmanager.mongodb import MongoManager
from handler import Router
from models import Employer, Vacancy
from repository import EmployerRepository, VacancyRepository
from settings.basic import mongo_settings, sql_engine
from src.parser import Parser

app = Flask(__name__)

session = sessionmaker(sql_engine)

mongo_manager = MongoManager(mongo_settings)

employers_id = mongo_manager.get_employers_id()

employers_repo = EmployerRepository(session, Employer)
vacancy_repo = VacancyRepository(session, Vacancy)

parser = Parser(employers_id)
parser.search_employers(employers_repo, Employer)
parser.search_vacancies(vacancy_repo, Vacancy)

db_manager = DBManager(session, Employer, Vacancy)

router = Router(db_manager, mongo_manager)

app.add_url_rule("/", "main", router.main)
app.add_url_rule(
    "/companies_and_vacancies",
    "companies_and_vacancies",
    router.companies_and_vacancies,
)
app.add_url_rule("/average_salary", "average_salary", router.avg_salary)
app.add_url_rule("/vacancies", "vacancies", router.vacancies)
app.add_url_rule(
    "/high_salary_vacancies",
    "high_salary_vacancies",
    router.vacancies_with_higher_salary,
)
app.add_url_rule(
    "/vacancies_with_keyword", "vacancies_with_keyword", router.vacancies_with_keyword
)
app.add_url_rule("/add_vacancies", "add_vacancies", router.add_vacancies)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
