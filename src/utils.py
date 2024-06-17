import psycopg2


def create_db(database_name: str):
    """Метод для создания базы данных"""
    conn = psycopg2.connect(user="postgres", host="localhost", password="postgres")
    cur = conn.cursor()
    conn.autocommit = True
    try:
        cur.execute(f"DROP DATABASE {database_name}")
    except Exception as er:
        print(f"{er}: Базы данных не существует")
    cur.execute(f"CREATE DATABASE {database_name};")

    cur.close()
    conn.close()


def create_table():
    """Метод для создания таблиц employers и vacancies"""

    conn = psycopg2.connect(dbname="hh_parser", user="postgres", host="localhost", password="postgres")
    with conn.cursor() as cur:
        try:
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS employers (
                employer_id SERIAL PRIMARY KEY,
                employer_name VARCHAR(255) unique NOT NULL
            )
                """
            )
        except Exception as err:
            print(f"{err}: Таблица существует")

    with conn.cursor() as cur:
        try:
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS vacancies (
                    vacancy_id serial primary key,
                    vacancy_name text NOT NULL,
                    salary int,
                    employer_id INT REFERENCES employers(employer_id)
                    )
                    """
            )
        except Exception as err:
            print(f"{err}: Таблица существует")
    conn.commit()
    conn.close()
