import logging
from datetime import date
currentdate = str(date.today())
logger = logging.getLogger("Nivetha")
logger.setLevel(logging.ERROR)
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
file_handler = logging.FileHandler(f"error_details_{currentdate}.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

logger_log = logging.getLogger("Nivi")
logger_log.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
file_handler = logging.FileHandler("login_details_"+currentdate+".log")
file_handler.setFormatter(formatter)
logger_log.addHandler(file_handler)
