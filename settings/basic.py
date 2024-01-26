from dataclasses import dataclass
from pathlib import Path

from environs import Env
from sqlalchemy import create_engine


@dataclass
class SQLEngineSettings:
    dialect: str
    driver: str
    user: str
    password: int
    host: str
    port: int
    db_name: str


@dataclass
class MongoEngineSettings:
    host: str
    db_name: str
    collection_name: str


@dataclass
class Settings:
    sql_engine_settings: SQLEngineSettings
    mongo_engine_settings: MongoEngineSettings


def get_engine_settings(path: Path) -> Settings:
    """
    Функция создаёт параметры для подключения к базам данных
    """
    env = Env()
    env.read_env(path)

    return Settings(
        SQLEngineSettings(
            dialect=env.str("DIALECT"),
            driver=env.str("DRIVER"),
            user=env.str("USER"),
            password=env.str("PASS"),
            host=env.str("SQL_HOST"),
            port=env.str("PORT"),
            db_name=env.str("DATABASE_NAME"),
        ),
        MongoEngineSettings(
            host=env.str("MONGODB_HOST"),
            db_name=env.str("DATABASE_NAME"),
            collection_name=env.str("COLLECTION_NAME"),
        ),
    )


def create_engine_url(sett: SQLEngineSettings) -> str:
    """
    Функция создаёт ссылку для подключения к SQL базе данных
    """
    return f"{sett.dialect}+{sett.driver}://{sett.user}:{sett.password}@{sett.host}:{sett.port}/{sett.db_name}"


ENGINE_PATH = Path(__file__).parent.parent.joinpath("engine_config")
SETTINGS = get_engine_settings(ENGINE_PATH)

ENGINE_URL = create_engine_url(SETTINGS.sql_engine_settings)
sql_engine = create_engine(ENGINE_URL)

mongo_settings = SETTINGS.mongo_engine_settings
