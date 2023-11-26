from api_classes.alliances_classes import SelectAlliancesData, InsertAllianceData, DeleteAllianceData

from log_module.log_app import viki_log
logger = viki_log("city_api")


def load_alliances(connection: dict, city_id: str) -> tuple[list, dict]:
    """
    Load all city_id's who have an alliance with the city
    :param connection: Open database connection
    :param city_id: The uuid from city
    :return: List of allied cities and the open database connection
    """
    try:
        connection['cursor'].execute(SelectAlliancesData.ALLIANCES.value, (city_id,))
        result: list = [row[0] for row in connection['cursor'].fetchall()]

    except Exception as e:
        logger.error(f"Alliances not found in database by error: {e} - Type: {type(e)}")
        result = []

    return result, connection


def insert_alliances(connection: dict, alliances: list, city_id: str) -> dict:
    """
    Identifies the existing bidirectional alliances for the city_id
    :param connection: Open database connection
    :param alliances: List of allied cities
    :param city_id: The uuid from city
    :return: The open database connection
    """
    try:
        for alliance_city in alliances:
            connection['cursor'].execute(InsertAllianceData.ALLIANCES.value, (
                city_id,
                alliance_city
            ))
            connection['cursor'].execute(InsertAllianceData.ALLIANCES.value, (
                alliance_city,
                city_id
            ))
        connection['conn'].commit()

    except Exception as e:
        logger.error(f"Failed to insert the alliance to the database by error: {e} - Type: {type(e)}")

    return connection


def delete_alliances(connection: dict, city_id: str) -> dict:
    """
    Deletes the existing alliances for the city_id on both sides
    :param connection: Open database connection
    :param city_id: The uuid from city
    :return: The open database connection
    """
    try:
        connection['cursor'].execute(DeleteAllianceData.ALLIANCES.value, (
            city_id, city_id
        ))
        connection['conn'].commit()

    except Exception as e:
        logger.error(f"Failed to delete the alliance from the database by error: {e} - Type: {type(e)}")

    return connection
