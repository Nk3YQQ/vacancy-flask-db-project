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


def check_salary(salary):
    if not salary:
        return "Нет данных"
    return salary


def handle_array(array):
    return list(
        map(
            lambda x: {
                "vacancy_name": x.vacancy_name,
                "employer_name": x.employer_name,
                "salary": check_salary(x.salary),
                "requirements": x.requirements,
            },
            array,
        )
    )


def validate(employer_id, employers):
    errors = {}

    if employer_id == '' or not employer_id:
        errors['employers'] = 'Поле не может быть пустым'

    if employer_id in employers:
        errors['employers'] = 'Данный работодатель уже находится в базе данных'

    return errors
