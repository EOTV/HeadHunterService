import os
from dotenv import load_dotenv

load_dotenv()

REGIONS_URL = os.environ.get("REGIONS_URL")

PATH_TO_DRIVER = os.environ.get("PATH_TO_DRIVER")
JOB_TITLE_PATH = os.environ.get("JOB_TITLE_PATH")

DATA_TRANSFER_FOLDER = os.environ.get("DATA_TRANSFER_FOLDER")

MOSCOW_REGION_CODE = os.environ.get("MOSCOW_REGION_CODE")
MOSCOW_AREA_CODE = os.environ.get("MOSCOW_AREA_CODE")
SPB_REGIONC_CODE = os.environ.get("SPB_REGIONC_CODE")