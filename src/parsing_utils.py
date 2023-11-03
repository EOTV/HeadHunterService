import requests
import config
import fake_useragent
from typing import List

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import re



def get_all_regions() -> List[str]:
    """
    Функция возвращающая, номера всех регионов в России.
    """
    user_agent = fake_useragent.UserAgent()
    regions = requests.get(
        url=config.REGIONS_URL,
        headers={"user_agent": user_agent.random}
    ).json()
    return [str(region["id"]) for region in regions[0]["areas"]]

def get_mean_salary(job_title: str) -> dict[str, dict[str, int]]:
    """
    Функция принимающая на вход профессию, и список всех регионов в России.
    Возвращает: {
        "job_title": {
            "mean_salary": int,
            "count_vacancies": int
    }}
    """
    user_agent = fake_useragent.UserAgent()
    mean_salary_by_region = []
    result_row = {}
    for region in get_all_regions():
        url = f"https://api.hh.ru/vacancies?clusters=true&only_with_salary=true&enable_snippets=true&st=searchVacancy' \
            '&text={job_title}&search_field=name&per_page=100&area={region}"
        vacancies = requests.get(
            url=url,
            headers={"user_agent": user_agent.random}                    
        ).json()
        for vacancy in vacancies["items"]:
            if vacancy["salary"]["from"] is None:
                continue
            mean_salary_by_region.append(vacancy["salary"]["from"])
            
    result_row[job_title] = {
        "Средняя зарплата.": int(sum(mean_salary_by_region) / len(mean_salary_by_region)),
        "Количество вакансий в России.": len(mean_salary_by_region) * config.VACANCY_FACTOR
    }
    return result_row

def get_count_vacancies(job_title: str):
    URL = fr'https://hh.ru/search/vacancy?text={job_title}'

    service = webdriver.ChromeService(executable_path='chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    driver.get(URL)

    el = driver.find_element(By.XPATH, "//h1[@data-qa='bloko-header-3']")
    return int(''.join(re.findall(r'\d+', el.text)))