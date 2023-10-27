import requests
import config
from typing import List

def get_all_regions() -> List[str]:
    """
    Функция возвращающая, номера всех регионов в России.
    """
    regions = requests.get(
        url=config.REGIONS_URL
    ).json()
    return [str(region["id"]) for region in regions[0]["areas"]]

def get_count_vacancies(job_title: str, regions: List[str]) -> dict[str, dict[str, int]]:
    """
    Функция принимающая на вход профессию, и список всех регионов в России.
    Возвращает: {
        "job_title": {
            "mean_salary": int,
            "count_vacancies": int
    }}
    """
    mean_salary_by_region = []
    result_row = {}
    for region in get_all_regions():
        url = f"https://api.hh.ru/vacancies?clusters=true&only_with_salary=true&enable_snippets=true&st=searchVacancy' \
            '&text={job_title}&search_field=name&per_page=100&area={region}"
        vacancies = requests.get(
            url=url                    
        ).json()
        for vacancy in vacancies["items"]:
            if vacancy["salary"]["from"] is None:
                continue
            mean_salary_by_region.append(vacancy["salary"]["from"])
            
    result_row[job_title] = {
        "Средняя зарплата.": int(sum(mean_salary_by_region) / len(mean_salary_by_region)),
        "Количество вакансий в России.": len(mean_salary_by_region)
    }
    return result_row