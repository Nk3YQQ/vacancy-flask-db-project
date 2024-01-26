from dbmanager.mongodb import MongoManager
from settings.basic import mongo_settings


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


def get_employers_id():
    return MongoManager(mongo_settings).get_employers_id()
