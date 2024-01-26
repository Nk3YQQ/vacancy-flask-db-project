from sqlalchemy import desc, func, nullslast

from src.utils import handle_array


class DBManager:
    def __init__(self, session, employer_model, vacancy_model):
        self._session = session
        self._employer_model = employer_model
        self._vacancy_model = vacancy_model

    def get_all_vacancies(self):
        with self._session() as session:
            query = (
                session.query(
                    self._vacancy_model.vacancy_name,
                    self._employer_model.employer_name,
                    self._vacancy_model.salary,
                    self._vacancy_model.requirements,
                )
                .join(self._vacancy_model)
                .order_by(nullslast(desc(self._vacancy_model.salary)))
                .all()
            )
            return handle_array(query)

    def get_companies_and_vacancies_count(self):
        with self._session() as session:
            query = (
                session.query(
                    self._employer_model.employer_name,
                    func.count(self._vacancy_model.vacancy_id),
                )
                .join(self._vacancy_model)
                .group_by(self._employer_model.employer_name)
                .order_by(nullslast(desc(func.count(self._vacancy_model.vacancy_id))))
                .all()
            )
            return list(map(lambda x: {"name": x[0], "vacancies": x[1]}, query))

    def get_avg_salary(self):
        with self._session() as session:
            return round(session.query(func.avg(self._vacancy_model.salary)).scalar())

    def get_vacancies_with_higher_salary(self):
        with self._session() as session:
            average_salary = self.get_avg_salary()
            high_salary_vacancies = (
                session.query(
                    self._vacancy_model.vacancy_name,
                    self._employer_model.employer_name,
                    self._vacancy_model.salary,
                    self._vacancy_model.requirements,
                )
                .join(self._employer_model)
                .filter(self._vacancy_model.salary > average_salary)
                .order_by(nullslast(desc(self._vacancy_model.salary)))
                .all()
            )
            return handle_array(high_salary_vacancies)

    def get_vacancies_with_keyword(self, keyword):
        with self._session() as session:
            query = (
                session.query(
                    self._vacancy_model.vacancy_name,
                    self._employer_model.employer_name,
                    self._vacancy_model.salary,
                    self._vacancy_model.requirements,
                )
                .join(self._employer_model)
                .filter(
                    self._vacancy_model.vacancy_name.ilike(f"%{keyword}%")
                    | self._vacancy_model.requirements.ilike(f"%{keyword}%")
                )
                .order_by(nullslast(desc(self._vacancy_model.salary)))
                .all()
            )
            return handle_array(query)
