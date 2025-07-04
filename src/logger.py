import logging
import os
from datetime import datetime

## creating log file name 
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}. log"

##log_file path name
LOGS_PATH = os.path.join(os.getcwd(), "logs",LOG_FILE)

##Create afile 
os.makedirs(LOGS_PATH,exist_ok=True)

## log file path 
LOG_FILE_PATH = os.path.join(LOGS_PATH,LOG_FILE)


logging.basicConfig(
    filename= LOG_FILE_PATH,
    format="[%(asctime)s] - Line:%(lineno)d - %(levelname)s - %(message)s",
    level= logging.INFO
)


