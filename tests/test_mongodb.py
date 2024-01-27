import pytest

from dbmanager.mongodb import MongoManager
from settings.basic import mongo_settings

mongo_manager = MongoManager(mongo_settings)


def test_get_employers_id():
    employers_id = mongo_manager.get_employers_id()
    assert isinstance(employers_id, list)


@pytest.fixture
def employer_id():
    return 123456


def test_add_employer(employer_id):
    mongo_manager.add_employer(employer_id)

    employers_id = mongo_manager.get_employers_id()

    assert employer_id in employers_id


def test_delete_employer(employer_id):
    mongo_manager.delete_employer(employer_id)

    employers_id = mongo_manager.get_employers_id()

    assert employer_id not in employers_id
