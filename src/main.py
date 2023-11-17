import time

import pandas as pd

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.service import Service
from selenium.webdriver import FirefoxOptions


from parsing_utils import get_info_by_vacancies
from parsing_utils import create_json_file

import config

def main():
    options = FirefoxOptions()
    options.add_argument("--headless")

    service = Service(executable_path=config.PATH_TO_DRIVER)

    driver = Firefox(service=service, options=options)

    result_data = {
        "VacanciesName": [],
        "CountVacancies": [],
        "MeanSalary": []
    }
    
    job_titles = pd.read_csv(config.JOB_TITLE_PATH)["prof_name"].values
    for job_title in job_titles:
        try:
            vacancies_name, count_vacancies, mean_salary = get_info_by_vacancies(
                job_title=job_title, driver=driver
            )

            result_data["VacanciesName"].append(vacancies_name)
            result_data["CountVacancies"].append(count_vacancies)
            result_data["MeanSalary"].append(mean_salary)

            print(
                f"| Название вакансии - {vacancies_name} | Кол-во вакансий - {count_vacancies} | Средняя зп - {mean_salary} |"
            )
        except:
            continue

    create_json_file(data=result_data, path_to_save=config.DATA_TRANSFER_FOLDER)

if __name__ == "__main__":
    main()