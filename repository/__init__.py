from abc import ABC, abstractmethod


class Repository(ABC):
    @abstractmethod
    def save(self, entity):
        pass

    @abstractmethod
    def content(self):
        pass

    @abstractmethod
    def find(self, entity, model):
        pass


class EmployerRepository(Repository):
    def __init__(self, session, model):
        self._session = session
        self._model = model

    def save(self, entity):
        with self._session() as session:
            session.add(entity)
            session.commit()

    def content(self):
        with self._session() as session:
            return session.query(self._model).all()

    def find(self, entity, model):
        with self._session() as session:
            potential_entity = (
                session.query(model)
                .filter(model.employer_id == entity.employer_id)
                .first()
            )
            return True if potential_entity else False


class VacancyRepository(Repository):
    def __init__(self, session, model):
        self._session = session
        self._model = model

    def save(self, entity):
        with self._session() as session:
            session.add(entity)
            session.commit()

    def content(self):
        with self._session() as session:
            return session.query(self._model).all()

    def find(self, entity, model):
        with self._session() as session:
            potential_entity = (
                session.query(model)
                .filter(model.vacancy_id == entity.vacancy_id)
                .first()
            )
            return True if potential_entity else False
