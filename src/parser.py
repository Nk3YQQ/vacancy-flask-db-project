import json
import logging

import requests

from src.utils import make_salary

logger = logging.getLogger(__name__)


class Parser:
    def __init__(self, employers_id: list[int], mongo_manager) -> None:
        self.employers_id = employers_id
        self._mongo_manager = mongo_manager
        self._employers_urls = list(map(lambda x: f"https://api.hh.ru/employers/{x}", self.employers_id))
        self._vacancies_urls = list(
            map(
                lambda x: f"https://api.hh.ru/vacancies?employer_id={x}&per_page=10",
                self.employers_id,
            )
        )

    def search_employers(self, repository, employer) -> None:
        logger.info("Start parsing employers...")
        for employer_url in self._employers_urls:
            raw_employer = json.loads(requests.get(employer_url).content)
            try:
                new_employer = employer(employer_id=raw_employer["id"], employer_name=raw_employer["name"])
            except KeyError:
                logger.error("Invalid id for employer.")
                self._mongo_manager.delete_employer(int(employer_url[28:]))
                logger.info("Invalid id was deleted by Mongo manager. Don't worry.")
            else:
                if repository.find(new_employer):
                    logger.info("Employer in database. Skipping it...")
                    continue
                else:
                    repository.save(new_employer)
                    logger.info("Employer has been added.")

    def search_vacancies(self, repository, vacancy) -> None:
        logger.info("Start parsing vacancies...")
        for vacancy_url in self._vacancies_urls:
            raw_vacancies = json.loads(requests.get(vacancy_url).content).get("items")
            if not raw_vacancies:
                logger.warning("Vacancy is empty. Skipping it...")
                continue
            for raw_vacancy in raw_vacancies:
                new_vacancy = vacancy(
                    vacancy_id=raw_vacancy["id"],
                    employer_id=raw_vacancy["employer"]["id"],
                    vacancy_name=raw_vacancy["name"],
                    salary=make_salary(raw_vacancy["salary"]),
                    requirements=raw_vacancy["snippet"]["requirement"],
                )
                if repository.find(new_vacancy):
                    logger.info("Vacancy in database. Skipping it...")
                    continue
                else:
                    repository.save(new_vacancy)
                    logger.info("Vacancy has been added.")
