import os
import psycopg2
from dotenv import load_dotenv

from log_module.log_app import viki_log

logger = viki_log("city_api")

load_dotenv()
db_params = {
    'host': os.getenv('PGHOST'),            # os.environ['PGHOST'],
    'port': os.getenv('PGPORT'),            # os.environ['PGPORT']
    'user': os.getenv('PGUSER'),            # os.environ['PGUSER'],
    'password': os.getenv('PGPASSWORD'),    # os.environ['PGPASSWORD'],
    'database': 'cities'
}


def connect_to_postgres() -> dict:
    """
    Open connection to postgres database
    :return: connection and cursor as dict
    """
    connection = None
    cursor = None

    try:
        connection = psycopg2.connect(**db_params)
        cursor = connection.cursor()

    except Exception as e:
        logger.error(f"No connection to database: {e} - Type: {type(e)}")

    return {"conn": connection, "cursor": cursor}


def disconnect_to_postgres(connection: dict) -> None:
    """
    Closed connection to postgres database
    :param connection: connection and cursor as dict
    :return: None
    """
    try:
        connection["cursor"].close()
        connection["conn"].close()
    except Exception as e:
        logger.error(f"Connection to database can't be closed: {e} - Type: {type(e)}")
