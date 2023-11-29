from flask import jsonify, Response

from common.error import forbidden, not_found
from log_module.log_app import viki_log
from sql_module.connection import connect_to_postgres, disconnect_to_postgres

logger = viki_log("city_api")


def execute_sql(connection: dict, execution: str) -> None:
    """
    Execute the sql command on database
    :param connection: connection and cursor as dict
    :param execution: execution sql command
    :return: None
    """
    try:
        connection["cursor"].execute(execution)
        connection["conn"].commit()

    except Exception as e:
        logger.error(f"Cannot execute command, with error message: {e} - Type: {type(e)}")


def execute_sql_by_script(sql_file_path) -> Response:
    """
    Execute sql command to postgres connection session
    :param sql_file_path: path to executable sql file
    :return: connection and cursor object
    """
    connection: dict = connect_to_postgres()

    try:
        with open(sql_file_path, 'r') as sql_file:
            sql_script: str = sql_file.read()

    except Exception as e:
        not_found(f"Cannot read file: {sql_file_path}, with error message: {e} - Type: {type(e)}")

    try:
        execute_sql(connection, sql_script)

    except Exception as e:
        forbidden(f"Cannot execute command from file: {sql_file_path}, with error message: {e} - Type: {type(e)}")

    disconnect_to_postgres(connection)

    return jsonify({'message': 'Database initialization successfully'}, 200)
