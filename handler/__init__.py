from typing import Any

from flask import redirect, render_template, request, url_for

from src.parser import Parser
from src.utils import validate


class Router:
    def __init__(self, db_manager, mongo_manager, employers_repo, vacancy_repo, employer, vacancy) -> None:
        self._employers_id = mongo_manager.get_employers_id()
        self._db_manager = db_manager
        self._mongo_manager = mongo_manager
        self._employers_repo = employers_repo
        self._vacancy_repo = vacancy_repo
        self._employer = employer
        self._vacancy = vacancy

    @staticmethod
    def main() -> Any:
        return render_template("main.html")

    def companies_and_vacancies(self) -> Any:
        return render_template(
            "companies.html",
            companies=self._db_manager.get_companies_and_vacancies_count(),
        )

    def vacancies(self) -> Any:
        return render_template("vacancies.html", vacancies=self._db_manager.get_all_vacancies())

    def avg_salary(self) -> Any:
        return render_template("average_salary.html", average_salary=self._db_manager.get_avg_salary())

    def vacancies_with_higher_salary(self) -> Any:
        return render_template(
            "high_salary_vacancies.html",
            vacancies=self._db_manager.get_vacancies_with_higher_salary(),
        )

    def vacancies_with_keyword(self) -> Any:
        keyword = request.args.get("vacancy", "").lower()
        return render_template(
            "vacancies_with_keyword.html",
            keyword=keyword,
            vacancies=self._db_manager.get_vacancies_with_keyword(keyword),
        )

    def add_employer(self) -> Any:
        if request.method == "POST":
            try:
                employer_id = int(request.form.get("id"))
            except (ValueError, TypeError):
                errors = {"employers": "Индитификатор работодателя не может быть в виде букв"}
                return render_template("add_vacancies.html", errors=errors), 422
            else:
                employers = self._mongo_manager.get_employers_id()
                errors = validate(employer_id, employers)
                if errors:
                    return render_template("add_vacancies.html", employer_id=employer_id, errors=errors), 422
                self._mongo_manager.add_employer(employer_id)
                parser = Parser(self._mongo_manager.get_employers_id(), self._mongo_manager)
                parser.search_employers(self._employers_repo, self._employer)
                parser.search_vacancies(self._vacancy_repo, self._vacancy)
                return redirect(url_for("add_employer"), code=302)
        return "Работодатель успешно добавлен!"

    @staticmethod
    def add_new_employer() -> Any:
        employer = ""
        errors = {}

        return render_template("add_vacancies.html", employer=employer, errors=errors)
