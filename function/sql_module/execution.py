from log_module.log_app import viki_log

logger = viki_log("city_api")


def execute_sql(connection: dict, execution: str) -> None:
    """
    Execute the sql command on database
    :param connection: connection and cursor as dict
    :param execution: execution sql command
    :return:
    """
    try:
        connection["cursor"].execute(execution)
        connection["conn"].commit()

        logger.info(f"Execution successfully")

    except Exception as e:
        logger.error(f"Cannot execute command, with error message: {e}")


def execute_sql_by_script(connection: dict, sql_file_path) -> dict:
    """
    Execute sql command to postgres connection session
    :param connection: connection and cursor as dict
    :param sql_file_path: path to executable sql file
    :return: connection and cursor object
    """
    try:
        with open(sql_file_path, 'r') as sql_file:
            sql_script: str = sql_file.read()
    except Exception as e:
        logger.error(f"Cannot read file: {sql_file_path}, with error message: {e}")

    try:
        execute_sql(connection, sql_script)
    except Exception as e:
        logger.error(f"Cannot execute command from file: {sql_file_path}, with error message: {e}")

    return connection
