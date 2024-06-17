import psycopg2


class DBManager:
    @staticmethod
    def get_companies_and_vacancies_count():
        """Метод получает список всех компаний и количество вакансий у каждой компании."""
        with psycopg2.connect(dbname="hh_parser", user="postgres", password="postgres", host="127.0.0.1") as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT company_name, COUNT(vacancy_name) FROM vacancies GROUP BY company_name;")
                data = cur.fetchall()
        conn.close()
        return data

    @staticmethod
    def get_all_vacancies():
        """Метод получает список всех вакансий с указанием названия компании,
        названия вакансии и зарплаты и ссылки на вакансию"""
        with psycopg2.connect(dbname="hh_parser", user="postgres", password="postgres", host="localhost") as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM vacancies;")
                data = cur.fetchall()
        conn.close()
        return data

    @staticmethod
    def get_avg_salary():
        """Метод получает среднюю зарплату по вакансиям."""
        with psycopg2.connect(dbname="hh_parser", user="postgres", password="postgres", host="localhost") as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT AVG(salary) FROM vacancies;")
                data = cur.fetchall()
        conn.close()
        return data

    @staticmethod
    def get_vacancies_with_higher_salary():
        """Метод получает список всех вакансий, у которых зарплата выше средней по всем вакансиям"""
        with psycopg2.connect(dbname="hh_parser", user="postgres", password="postgres", host="localhost") as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT vacancy_name FROM vacancies WHERE salary > (SELECT AVG(salary) FROM vacancies);")
                data = cur.fetchall()
        conn.close()
        return data

    @staticmethod
    def get_vacancies_with_keyword(keyword: str):
        """Метод получает список всех вакансий,
        в названии которых содержатся переданные в метод слова,
        например python."""
        with psycopg2.connect(dbname="hh_parser", user="postgres", password="postgres", host="localhost") as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT vacancy_name FROM vacancies WHERE LOWER(vacancy_name) LIKE LOWER(%s)",
                    ("%" + keyword + "%",),
                )
                data = cur.fetchall()
        conn.close()
        return data
