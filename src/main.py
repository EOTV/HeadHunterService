import pandas as pd

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.service import Service
from parsing_utils import get_info_by_vacancies

def main():
    service = Service(executable_path="./repositories/geckodriver")
    driver = Firefox(service=service)

    job_titles = pd.read_csv('./repositories/proffesions.csv')["prof_name"].values
    for job_title in job_titles:
        result = get_info_by_vacancies(job_title="Оператор дрона", driver=driver)
        print(result)

if __name__ == "__main__":
    main()