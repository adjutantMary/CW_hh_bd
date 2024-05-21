import psycopg2


class DBManager:
    @staticmethod
    def get_companies_and_vacancies_count():
        """Метод получает список всех компаний и количество вакансий у каждой компании."""
        pass

    @staticmethod
    def get_all_vacancies():
        """Метод получает список всех вакансий с указанием названия компании,
        названия вакансии и зарплаты и ссылки на вакансию"""
        pass

    @staticmethod
    def get_avg_salary():
        """Метод получает среднюю зарплату по вакансиям."""
        pass

    @staticmethod
    def get_vacancies_with_higher_salary():
        """Метод получает список всех вакансий, у которых зарплата выше средней по всем вакансиям"""
        pass

    @staticmethod
    def get_vacancies_with_keyword():
        """Метод получает список всех вакансий,
        в названии которых содержатся переданные в метод слова,
        например python."""
        pass
