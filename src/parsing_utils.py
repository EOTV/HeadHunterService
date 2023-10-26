import requests
import numpy as np
import fake_useragent

import config

def get_all_regions() -> np.array:
    """
    Функция возвращающая, номера всех регионов в России.
    """
    user_agent = fake_useragent.UserAgent()
    regions = requests.get(
        url=config.REGIONS_URL,
        headers={"user_agent": user_agent.random}
    ).json()

    area_id = np.array([])
    for region in regions[0]["areas"]:
        area_id = np.append(area_id, int(region["id"]))
        
    return area_id