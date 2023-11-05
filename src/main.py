import pandas as pd

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.service import Service
from parsing_utils import get_info_by_vacancies
from parsing_utils import create_json_file

def main():
    service = Service(executable_path="./repositories/geckodriver")
    driver = Firefox(service=service)

    result_data = []

    job_titles = pd.read_csv('./repositories/proffesions.csv')["prof_name"].values
    for job_title in job_titles[:2]:
        result_data.append(get_info_by_vacancies(job_title=job_title, driver=driver))

    create_json_file(data=result_data, path_to_save="../")
    print("Done.")

if __name__ == "__main__":
    main()