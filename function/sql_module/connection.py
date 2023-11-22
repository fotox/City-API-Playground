import os
import psycopg2

from log_module.log_app import viki_log

logger = viki_log("city_api")

db_params = {
    'host': os.environ['PGHOST'],
    'database': 'cities',
    'user': os.environ['PGUSER'],
    'password': os.environ['PGPASSWORD'],
    'port': os.environ['PGPORT']
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

    connection = {
        "conn": connection,
        "cursor": cursor
    }

    return connection


def cancel_connection_to_postgres(connection: dict) -> None:
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
