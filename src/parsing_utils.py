import re
import json
import requests
import fake_useragent
from typing import List

from selenium.webdriver.common.by import By

import config

def get_info_by_vacancies(
        job_title: str, 
        driver
    ) -> dict[str, dict[str, int]]:
    """
    Функция принимающая на вход профессию, и список всех регионов в России.
    Возвращает: {
        "job_title": {
            "mean_salary": int,
            "count_vacancies": int
    }}
    """
    def get_all_regions() -> List[str]:
        """
        Функция возвращающая, номера всех регионов в России.
        """
        user_agent = fake_useragent.UserAgent()
        regions = requests.get(
            url=config.REGIONS_URL,
            headers={"user_agent": user_agent.random}
        ).json()
        return [int(region["id"]) for region in regions[0]["areas"]]
    
    def get_count_vacancies(job_title: str) -> int:
        url = fr'https://hh.ru/search/vacancy?text={job_title}'
        driver.get(
            url                    
        )

        el = driver.find_element(By.XPATH, "//h1[@data-qa='bloko-header-3']")
        return int(''.join(re.findall(r'\d+', el.text)))
    
    mean_salary_by_region = []

    user_agent = fake_useragent.UserAgent()

    for region in [config.MOSCOW_REGION_CODE, config.MOSCOW_AREA_CODE, config.SPB_REGIONC_CODE]:
        url = f"https://api.hh.ru/vacancies?clusters=true&only_with_salary=true&enable_snippets=true&st=searchVacancy' \
            '&text={job_title}&search_field=name&per_page=100&area={region}"
        
        headers = requests.utils.default_headers()
        headers.update({"User-Agent": user_agent.random})
        vacancies = requests.get(
            url=url,
            headers=headers                   
        ).json()

        try:
            for vacancy in vacancies["items"]:
                if vacancy["salary"]["from"] is None:
                    continue
            mean_salary_by_region.append(vacancy["salary"]["from"])
        except:
            continue
    
    try:
        vacancies_name = job_title
        count_vacancies = int(sum(mean_salary_by_region) / len(mean_salary_by_region))
        mean_salary = get_count_vacancies(job_title=job_title)

        return vacancies_name, count_vacancies, mean_salary
    except:
        vacancies_name = job_title
        count_vacancies = 0
        mean_salary = "Не найденно."

        return vacancies_name, count_vacancies, mean_salary

def create_json_file(data: dict, path_to_save: str="./") -> None:
    with open(path_to_save + "output.json", "w") as output_file:
        json.dump(data, output_file, ensure_ascii=False)