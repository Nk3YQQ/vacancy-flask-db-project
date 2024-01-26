import pymongo

from settings.basic import MongoEngineSettings


class MongoManager:
    def __init__(self, mongo_settings: MongoEngineSettings) -> None:
        self._con = pymongo.MongoClient(mongo_settings.host)
        self._db = self._con[mongo_settings.db_name]
        self._collection = self._db[mongo_settings.collection_name]

    def get_employers_id(self) -> list:
        """
        Метод возвращает список с id работодателей hh.ru
        """
        return list(self._collection.find())[0].get("employers_id")
