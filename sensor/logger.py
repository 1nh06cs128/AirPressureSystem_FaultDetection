import logging
import os
from datetime import datetime

#Log fileName
LOG_FILE_NAME = f"{datetime.now().strftime('%m%d%Y__%H%M%S')}.log"

#Logs Directory
LOG_FILE_DIR = os.path.join(os.getcwd(), "logs")

# create logs folder if not available
os.makedirs(LOG_FILE_DIR, exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG_FILE_DIR, LOG_FILE_NAME)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format=,
    level=logging.DEBUG
)