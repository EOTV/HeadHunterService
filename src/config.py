import os
from dotenv import load_dotenv

load_dotenv()

REGIONS_URL = os.environ.get("REGIONS_URL")
VACANCY_FACTOR = os.environ.get("VACANCY_FACTOR")