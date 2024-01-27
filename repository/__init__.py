from abc import ABC, abstractmethod
from typing import Any


class Repository(ABC):
    @abstractmethod
    def save(self, entity) -> None:
        pass

    @abstractmethod
    def content(self) -> None:
        pass

    @abstractmethod
    def find(self, entity) -> None:
        pass

    @abstractmethod
    def delete(self, entity) -> None:
        pass


class EmployerRepository(Repository):
    def __init__(self, session, model) -> None:
        self._session = session
        self._model = model

    def save(self, entity) -> None:
        with self._session() as session:
            session.add(entity)
            session.commit()

    def content(self) -> list[Any]:
        with self._session() as session:
            return session.query(self._model).all()

    def find(self, entity) -> bool:
        with self._session() as session:
            potential_entity = session.query(self._model).filter(self._model.employer_id == entity.employer_id).first()
            return True if potential_entity else False

    def delete(self, entity) -> None:
        with self._session() as session:
            entity = session.query(self._model).filter(self._model.employer_id == entity.employer_id).first()
            session.delete(entity)
            session.commit()


class VacancyRepository(Repository):
    def __init__(self, session, model) -> None:
        self._session = session
        self._model = model

    def save(self, entity) -> None:
        with self._session() as session:
            session.add(entity)
            session.commit()

    def content(self) -> list[Any]:
        with self._session() as session:
            return session.query(self._model).all()

    def find(self, entity) -> bool:
        with self._session() as session:
            potential_entity = session.query(self._model).filter(self._model.vacancy_id == entity.vacancy_id).first()
            return True if potential_entity else False

    def delete(self, entity) -> None:
        with self._session() as session:
            entity = session.query(self._model).filter(self._model.employer_id == entity.employer_id).first()
            session.delete(entity)
            session.commit()
