import logging
from logging.handlers import TimedRotatingFileHandler
import zipfile
import os
import datetime


SCRIPT_PATH: str = os.path.dirname(os.path.realpath(__file__))

if os.name == 'posix':
    SCRIPT_PATH = "/var/log/"


def viki_log(module_name: str) -> logging.Logger:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    log_file = f"{SCRIPT_PATH}\\current\\{module_name}.log"
    handler = TimedRotatingFileHandler(log_file, when="midnight", interval=1, backupCount=30, encoding="utf-8")
    formatter = logging.Formatter(fmt='%(levelname)s | %(asctime)s | %(message)s', datefmt='%Y-%m-%dT%H:%M:%SZ')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    if handler.shouldRollover(None):
        if os.path.getsize(log_file) > 0:
            yesterday_date = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y%m%d")
            zip_filename = f"{SCRIPT_PATH}\\archive\\{module_name}_logs\\{module_name}_log_{yesterday_date}.zip"

            with zipfile.ZipFile(zip_filename, 'w') as zip_file:
                zip_file.write(log_file, os.path.basename(log_file))

            os.remove(log_file)

    return logger
