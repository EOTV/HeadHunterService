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

    result_data = []

    job_titles = pd.read_csv(config.JOB_TITLE_PATH)["prof_name"].values
    for job_title in job_titles[:2]:
        current_vacancies = get_info_by_vacancies(job_title=job_title, driver=driver)

        result_data.append(current_vacancies)

        print(current_vacancies)

    create_json_file(data=result_data, path_to_save=config.DATA_TRANSFER_FOLDER)

if __name__ == "__main__":
    main()