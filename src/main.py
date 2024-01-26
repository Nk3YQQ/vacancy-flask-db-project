from repository import EmployerRepository, VacancyRepository
from src.parser import Parser
from src.utils import get_employers_id
from settings.basic import sql_engine
from models import Employer, Vacancy

employers_repo = EmployerRepository(sql_engine, Employer)
vacancy_repo = VacancyRepository(sql_engine, Vacancy)

employers_id = get_employers_id()

parser = Parser(employers_id)

parser.search_employers(employers_repo, Employer)
parser.search_vacancies(vacancy_repo, Vacancy)
