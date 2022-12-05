
  <h3 align="center">Сервис для проведения тестирования</h3>

### Используемый стек технологий в проекте:
* Django
* PostgreSQL
* Bootstrap
* Docker
* Poetry
* pre-commit
* ...

### Перед запуском выполните:
* Склонировать репозиторий в локальную директорию:
  ```sh
  git clone https://github.com/Stanis96/examination_service.git
  ```
* Виртуальное окружение:
  ```sh
  poetry config virtualenvs.in-project true
  poetry install
  ```
* В корне проекта создайте ```.env``` и задайте значения переменных:
    ```sh
    DJANGO_SECRET_KEY=
    DJANGO_ALLOWED_HOSTS=#localhost

    DB_NAME=
    DB_USER=
    DB_PASSWORD=
    DB_HOST=
    DB_PORT=

    DEBUG=
    ```
* Cоздание и применение миграций:
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```
