def make_salary(salary: dict) -> int:
    """
    Функция принимает словарь, берёт данные из блока "Зарплата" и преобразует в строку
    """
    if not salary:
        return None
    if not salary["to"]:
        return int(salary["from"])
    elif not salary["from"]:
        return int(salary["to"])
    else:
        return round(int(salary["to"]) + int(salary["from"]) / 2)


def handle_array(array):
    return list(
        map(
            lambda x: {
                "vacancy_id": x.vacancy_id,
                "employer_id": x.employer_id,
                "name": x.name,
                "salary": x.salary,
                "requirements": x.requirements,
            },
            array,
        )
    )
