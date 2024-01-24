import requests
import json


class Parser:
    def __init__(self, employers_id):
        self.employers_id = employers_id
        self._employers_urls = list(map(lambda x: f"https://api.hh.ru/employers/{x}", self.employers_id))
        self._vacancies_urls = list(map(lambda x: f"https://api.hh.ru/vacancies?employer_id={x}&per_page=10",
                                        self.employers_id))

    def search_employers(self):
        employers_list: list = []
        for employer_url in self._employers_urls:
            raw_employer = json.loads(requests.get(employer_url).content)
            employers = {"id": raw_employer["id"], "name": raw_employer["name"]}
            employers_list.append(employers)
        return employers_list

    def search_vacancies(self):
        vacancies_list: list = []
        for vacancy_url in self._vacancies_urls:
            raw_vacancies = json.loads(requests.get(vacancy_url).content).get('items')
            vacancies = list(map(
                lambda x: {
                    "id": x.get('id'),
                    "name": x.get('name'),
                    'salary': x.get('salary'),
                    'description': x.get('description'),
                    'requirements': x['snippet']['requirement']
                },
                raw_vacancies
            )
            )
            vacancies_list.extend(vacancies)
        return vacancies_list
