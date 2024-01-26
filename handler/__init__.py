from flask import render_template, request


class Router:
    def __init__(self, db_manager, mongo_manager):
        self._db_manager = db_manager
        self._mongo_manager = mongo_manager

    @staticmethod
    def main():
        return render_template("main.html")

    def companies_and_vacancies(self):
        return render_template(
            "companies.html",
            companies=self._db_manager.get_companies_and_vacancies_count(),
        )

    def vacancies(self):
        return render_template(
            "vacancies.html", vacancies=self._db_manager.get_all_vacancies()
        )

    def avg_salary(self):
        return render_template(
            "average_salary.html", average_salary=self._db_manager.get_avg_salary()
        )

    def vacancies_with_higher_salary(self):
        return render_template(
            "high_salary_vacancies.html",
            vacancies=self._db_manager.get_vacancies_with_higher_salary(),
        )

    def vacancies_with_keyword(self):
        keyword = request.args.get("vacancy", "").lower()
        return render_template(
            "vacancies_with_keyword.html",
            keyword=keyword,
            vacancies=self._db_manager.get_vacancies_with_keyword(keyword),
        )

    def add_vacancies(self):
        employer_id = request.args.get("id")
        self._mongo_manager.add_vacancies(employer_id)
        return render_template("add_vacancies.html", employer_id=employer_id)
