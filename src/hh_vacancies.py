import psycopg2
import requests


class HH_data_getter:
    """Класс для получения данных по API HH.ru"""

    employers = {
        "СБЕР": "3529",
        "МТС": "3776",
        "Умскул": "4557535",
        "Тинькофф": "78638",
        "99 БАЛЛОВ": "4406715",
        "Банк ВТБ (ПАО)": "4181",
        "Яндекс Крауд": "9498112",
        "Газпромбанк": "3388",
        "ПАО Татнефть": "575665",
        "ПАО ТАТТЕЛЕКОМ": "672459",
    }

    def get_employers(self, emp_id: int) -> list[dict]:
        """
        Метод реализует поиск работодателей при наличии зп и вакансий
        :param emp_id: id компании (работодателя)
        :return: list[dict] компаний
        """
        params = {
            "page": 1,
            "per_page": 100,
            "emp_id": emp_id,
            "only_with_salary": True,
            "area": 113,
            "only_with_vacancies": True,
        }
        return requests.get("https://api.hh.ru/vacancies/", params=params).json()["items"]

    def get_vacancies_list(self):
        """
        Метод формирует список вакансий в зависимости от выбранных компаний в списке
        :return: vacancies_list: list
        """
        vacancies_list = []

        for employer in self.employers:
            response_vacancies = self.get_employers(self.employers[employer])
            for vacancy in response_vacancies:
                if vacancy["salary"]["from"] is None:
                    salary = 0
                else:
                    salary = vacancy["salary"]["from"]

                vacancies_list.append(
                    {
                        "url": vacancy["alternate_url"],
                        "salary": salary,
                        "vacancy_name": vacancy["name"],
                        "employer": employer,
                    }
                )
        return vacancies_list

    def vacancies_to_db(self):
        with psycopg2.connect(dbname='hh_parcer', user='lacrimosa',
                              password='jett_loves_sql40', host='localhost') as conn:
            with conn.cursor() as cur:
                for vacancy in self.get_vacancies_list():
                    cur.execute(
                        f'INSERT INTO vacancies(vacancy_name, salary, company_name, vacancy_url) values'
                        f"('{vacancy['vacancy_name']}', '{int(vacancy['salary'])}',"
                        f"'{vacancy['employer']}', '{vacancy['url']}')"
                    )
        conn.commit()
        conn.cursor()

    def employers_to_db(self):
        with psycopg2.connect(dbname='hh_parcer', user='lacrimosa',
                              password='jett_loves_sql40', host='localhost') as conn:
            with conn.cursor() as cur:
                for employer in self.employers:
                    cur.execute(f'INSERT INTO companies values ('
                                f'"{int(self.employers[employer])}", "{employer}")')
                    conn.commit()
                    conn.close()




# cls_obj = HH_data_getter()
# test_1 = cls_obj.get_employers_list()
# print(test_1)
