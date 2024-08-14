Добро пожаловать на страницу описания проекта "vacancy-flask-db-project"! Данный проект явялется сырым прототипом приложения для анализа вакансий. За основу взят веб-фреймворк Flask. 

Базу данных для хранения вакансий и компаний вы можете использовать любую, так как CRUD-операции реализованы с помощью SQLAlchemy (в большей стпепени - ORM).

Но база данных для хранения id компаний используется NoSQL - MongoDB, поэтому желательно использовать её.

Проект поделён на 8 пакетов - dbmanager (отвечает за реализацию статистических запросов в SQL базу данных), handler (хранит в себе класс, отвечающий за хранения маршрутов приложения (регистрация маршрутов реализована в src.main.py)), logger (отвечает за конфигурацию логов приложения),
models (хранит в себе базовую модель, модель работодателя и вакансии), settings (настройки приложения, куда подгружаются все данные из обычного файла (можно подстроить под .env файл)), src (основной пакет, где хранятся шаблоны для обработчиков, парсер, функции и main.py),
а также tests (хранит в себя некоторые тесты интрейфейсов).

Всю информацию о зависимостях можно найти в файлах poetry.lock и pyproject.toml.

Конфигурация для flake8 назодится в файле .flake8.

Основные параметры, которые необходимо указывать в файле engine_settings для настройки приложения:
1) DIALECT - диалект для реляционной СУБД;
2) DRIVER - то, что исподьзуется пол копотом (в данном примере - библеотека psycopg2);
3) USER - имя пользователя в СУБД;
4) PASS - пароль;
5) SQL_HOST - хост для реляционной СУБД;
6) MONGODB_HOST - хост для подлючения к базе данных MongoDB;
7) PORT - порт для подключения к SQL базе данных;
8) DATABASE_NAME - имя реляционной базы данных;
9) COLLECTION_NAME - имя коллекции MongoDB
10) EMPLOYERS_OBJECT_ID - id объекта с данными об id работодателей в MongoDB

Коллекция в базе данных MongoDB должна содержать один документ, который выгядит следующим образом: {employer_id: []}. В массиве должны содержаться id вакансий для корректной работы программы.

При старте приложения используется порт 5000, но Вы можете изменить его на свой.

Попадая на сайт, можно встретить заголовки, для которых реализованы методы в пакете dbmanager.

Не рекомендуется добавлять неправильные id и id в виде строк. Но если вы это сделаете, приложения выдаст Вам информацию, что "работник добавлен", но проверев базу данных, вы обнаружете, что его id там нет, так как реализован механизм автоматического удаления неверных id.

Также важным моментом является то, что если вы попытаетесь добавить работодателя, у которого при api-запросе вакансий нет, то информация о нём (не о вакансиях) будет в базе данных, но в разделах анализа не будет. Этот баг в дальнейшем будет исправлен.
