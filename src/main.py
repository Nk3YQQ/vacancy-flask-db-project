from sqlalchemy.orm import sessionmaker

from dbmanager import DBManager
from dbmanager.mongodb import MongoManager
from models import Employer, Vacancy
from repository import EmployerRepository, VacancyRepository
from settings.basic import mongo_settings, sql_engine
from src.parser import Parser

session = sessionmaker(sql_engine)

employers_repo = EmployerRepository(session, Employer)
vacancy_repo = VacancyRepository(session, Vacancy)

employers_id = MongoManager(mongo_settings).get_employers_id()

parser = Parser(employers_id)

# parser.search_employers(employers_repo, Employer)
# parser.search_vacancies(vacancy_repo, Vacancy)

db_manager = DBManager(session, Employer, Vacancy)
