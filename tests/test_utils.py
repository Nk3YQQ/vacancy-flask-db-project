from dataclasses import dataclass

import pytest

from src.utils import check_salary, handle_array, make_salary, validate


@pytest.fixture
def salary_1() -> dict:
    return {"from": 20000, "to": None, "currency": "RUR", "gross": False}


@pytest.fixture
def salary_2() -> dict:
    return {"from": 20000, "to": 40000, "currency": "RUR", "gross": False}


@pytest.fixture
def salary_3() -> None:
    return None


@pytest.fixture
def salary_4() -> dict:
    return {"from": None, "to": 40000, "currency": "RUR", "gross": False}


def test_make_salary(salary_1: dict, salary_2: dict, salary_3: None, salary_4: dict) -> None:
    assert make_salary(salary_1) == 20000
    assert make_salary(salary_2) == 50000
    assert make_salary(salary_3) is None
    assert make_salary(salary_4) == 40000


def test_check_salary(salary_1: dict, salary_2: dict, salary_3: None, salary_4: dict) -> None:
    assert check_salary(salary_1) == salary_1
    assert check_salary(salary_2) == salary_2
    assert check_salary(salary_3) == "Нет данных"
    assert check_salary(salary_4) == salary_4


@dataclass
class UnitedVacancy:
    vacancy_name: str
    employer_name: str
    salary: int
    requirements: str


@pytest.fixture
def array() -> list[UnitedVacancy]:
    return [
        UnitedVacancy(
            vacancy_name="Python Developer",
            employer_name="Компания N",
            salary=150000,
            requirements="Python, PostgreSQL, Git...",
        ),
        UnitedVacancy(
            vacancy_name="Java Developer",
            employer_name="Компания Z",
            salary=150000,
            requirements="Java, Spring, Git...",
        ),
    ]


def test_handle_array(array: list[UnitedVacancy]) -> None:
    vacancy_info = handle_array(array)
    assert isinstance(vacancy_info, list)
    assert isinstance(vacancy_info[0], dict)


@pytest.fixture
def employers() -> list[int]:
    return [1, 2, 3, 4, 5]


@pytest.fixture
def employer_1() -> int:
    return 2


@pytest.fixture
def employer_2() -> str:
    return ""


@pytest.fixture
def employer_3() -> None:
    return None


@pytest.fixture
def employer_4() -> int:
    return 6


def test_validate(employers: list[int], employer_1: int, employer_2: str, employer_3: None, employer_4: int) -> None:
    assert validate(employer_1, employers) == {"employers": "Данный работодатель уже находится в базе данных"}
    assert validate(employer_2, employers) == {"employers": "Поле не может быть пустым"}
    assert validate(employer_2, employers) == {"employers": "Поле не может быть пустым"}
    assert validate(employer_4, employers) == {}
