import json

import requests

from src.utils import make_salary


class Parser:
    def __init__(self, employers_id):
        self.employers_id = employers_id
        self._employers_urls = list(
            map(lambda x: f"https://api.hh.ru/employers/{x}", self.employers_id)
        )
        self._vacancies_urls = list(
            map(
                lambda x: f"https://api.hh.ru/vacancies?employer_id={x}&per_page=10",
                self.employers_id,
            )
        )

    def search_employers(self, repository, employer):
        for employer_url in self._employers_urls:
            raw_employer = json.loads(requests.get(employer_url).content)
            new_employer = employer(
                employer_id=raw_employer["id"], employer_name=raw_employer["name"]
            )
            if repository.find(new_employer, employer):
                continue
            else:
                repository.save(new_employer)

    def search_vacancies(self, repository, vacancy):
        for vacancy_url in self._vacancies_urls:
            raw_vacancies = json.loads(requests.get(vacancy_url).content).get("items")
            for raw_vacancy in raw_vacancies:
                new_vacancy = vacancy(
                    vacancy_id=raw_vacancy["id"],
                    employer_id=raw_vacancy["employer"]["id"],
                    vacancy_name=raw_vacancy["name"],
                    salary=make_salary(raw_vacancy["salary"]),
                    requirements=raw_vacancy["snippet"]["requirement"],
                )
                if repository.find(new_vacancy, vacancy):
                    continue
                else:
                    repository.save(new_vacancy)
