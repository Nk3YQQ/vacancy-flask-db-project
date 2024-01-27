from flask import Flask
from sqlalchemy.orm import sessionmaker

from dbmanager import DBManager
from dbmanager.mongodb import MongoManager
from handler import Router
from models import Employer, Vacancy
from repository import EmployerRepository, VacancyRepository
from settings.basic import mongo_settings, sql_engine
from logger import setup_logging

logger = setup_logging()

app = Flask(__name__)

session = sessionmaker(sql_engine)

mongo_manager = MongoManager(mongo_settings)

employers_repo = EmployerRepository(session, Employer)
vacancy_repo = VacancyRepository(session, Vacancy)

db_manager = DBManager(session, Employer, Vacancy)

router = Router(db_manager, mongo_manager, employers_repo, vacancy_repo, Employer, Vacancy)

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
app.add_url_rule("/add_employer", "add_employer", router.add_employer, methods=['GET', 'POST'])
app.add_url_rule('/add_new_employer', 'add_new_employer', router.add_new_employer)


if __name__ == "__main__":
    logger.info('Start app...')
    app.run(debug=True, port=5000)
