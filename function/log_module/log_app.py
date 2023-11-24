import logging
from logging.handlers import TimedRotatingFileHandler
import os
import shutil
import zipfile
import datetime

SCRIPT_PATH: str = os.path.dirname(os.path.realpath(__file__))

if os.name == 'posix':
    SCRIPT_PATH = "/var/log/"

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

if not logger.handlers:
    log_file = f"{SCRIPT_PATH}\\current\\example.log"
    handler = TimedRotatingFileHandler(log_file, when="midnight", interval=1, backupCount=30, encoding="utf-8")
    formatter = logging.Formatter(fmt='%(levelname)s | %(asctime)s | %(message)s', datefmt='%Y-%m-%dT%H:%M:%SZ')
    handler.setFormatter(formatter)
    logger.addHandler(handler)


def viki_log(module_name: str) -> logging.Logger:
    if handler.shouldRollover(None):
        if os.path.getsize(log_file) > 0:
            yesterday_date = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y%m%d")
            archive_dir = f"{SCRIPT_PATH}\\archive\\{module_name}_logs"
            zip_filename = f"{archive_dir}\\{module_name}_log_{yesterday_date}.zip"

            if not os.path.exists(archive_dir):
                os.makedirs(archive_dir)

            log_copy = f"{SCRIPT_PATH}\\archive\\temp_{module_name}_log_copy.log"
            shutil.copy(log_file, log_copy)

            if not os.path.exists(zip_filename):
                with zipfile.ZipFile(zip_filename, 'w') as file:
                    pass

            with zipfile.ZipFile(zip_filename, 'w') as zip_file:
                zip_file.write(log_copy, os.path.basename(zip_filename))

            os.remove(log_copy)
            with open(log_file, 'w'):
                pass

    return logger
