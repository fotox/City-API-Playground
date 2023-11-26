import uuid
from flask import jsonify, Response

from api_classes.alliances_classes import SelectAlliancesData
from api_classes.beauty_score_classes import SelectBeautyData
from api_classes.city_classes import SelectCityData, DeleteCityData, InsertCityData, UpdateCityData
from common.error import conflict, not_found
from common.events import load_alliances, insert_alliances, delete_alliances
from common.process import convert_city_response, calculate_allied_power
from sql_module.connection import connect_to_postgres, disconnect_to_postgres

from log_module.log_app import viki_log
logger = viki_log("city_api")


def get_beauty_score(beauty: str | int) -> int:
    """
    Look into database table beauty_score to find a match by beauty description or name.
    :param beauty: ID or description
    :return: ID of existing beauty code
    """
    connection: dict = connect_to_postgres()
    beauty_score: int = 0

    try:
        if isinstance(beauty, str):
            connection['cursor'].execute(SelectBeautyData.BEAUTY_SCORE_BY_NAME.value, (beauty,))
        else:
            connection['cursor'].execute(SelectBeautyData.BEAUTY_NAME_BY_SCORE.value, (beauty,))
            _beauty_name: str = connection['cursor'].fetchall()[0]
            beauty_score = beauty

    except Exception as e:
        logger.error(f"Beauty code or name not found by error: {e} - Type: {type(e)}")

    finally:
        disconnect_to_postgres(connection)

    return beauty_score


def get_city_from_database(city_id: str = None) -> Response:
    """
    Look into database table city to find a match by city_id.
    :param city_id: The uuid from city
    :return: List of cities there found in database
    """
    connection: dict = connect_to_postgres()
    city_list: list = []
    city_data: list = []
    message: str = ""

    try:
        if city_id is None:
            connection['cursor'].execute(SelectCityData.CITIES.value)
            city_data = [convert_city_response(*row) for row in connection['cursor'].fetchall()]
            message = 'Cities found successfully'
        else:
            connection['cursor'].execute(SelectCityData.CITY.value, (city_id,))
            city_data = [convert_city_response(*row) for row in connection['cursor'].fetchall()]
            connection['cursor'].execute(SelectAlliancesData.ALLIANCES.value, (city_id,))
            alliances: list = [row[0] for row in connection['cursor'].fetchall()]
            city_data[0]['allied_power'] = calculate_allied_power(connection,
                                                                  city_id,
                                                                  city_data[0]['geo_location_latitude'],
                                                                  city_data[0]['geo_location_longitude'],
                                                                  alliances)
            message = 'Cities found successfully'

    except Exception as e:
        not_found(f"City id not found by error: {e} - Type: {type(e)}")

    for city in city_data:
        alliances, connection = load_alliances(connection, city['city_uuid'])
        city['allied_cities'] = alliances
        city_list.append(city)

    disconnect_to_postgres(connection)

    return jsonify({
        'message': message,
        'body': city_list}, 200)


def delete_city_from_database(city_id: str) -> Response:
    """
    Look into database table city to find a match by city_id and delete the city and the coupled alliances.
    :param city_id: The uuid from city
    :return: Information message to confirm successful deletion
    """
    connection: dict = connect_to_postgres()
    try:
        connection['cursor'].execute(DeleteCityData.CITY.value, (city_id, city_id, city_id,))
        connection['conn'].commit()

    except Exception as e:
        not_found(f"Delete not complete. City id not found by error: {e} - Type: {type(e)}")

    disconnect_to_postgres(connection)

    return jsonify({
        'message': 'City and coupled alliances successfully deleted'}, 200)


def insert_city_into_database(dataset: dict) -> Response:
    """
    Create a new city and optional given alliances into the database.
    :param dataset: Dict of default information from city. Look to '<repo-root>/README.md' to visit the setup
    :return: City which has been added into the database
    """
    connection: dict = connect_to_postgres()
    beauty_score: int = get_beauty_score(dataset.get('beauty'))
    city_gen_uuid: str = str(uuid.uuid4())
    city_data: dict = {}

    try:
        connection['cursor'].execute(InsertCityData.CITY.value, (
            city_gen_uuid,
            dataset.get('name'),
            dataset.get('geo_location_latitude'),
            dataset.get('geo_location_longitude'),
            beauty_score,
            dataset.get('population')
        ))

        if dataset.get('allied_cities') is not None:
            insert_alliances(connection, dataset.get('allied_cities'), city_gen_uuid)

        connection['conn'].commit()

    except Exception as e:
        conflict(f"City can't be created by error: {e} - Type: {type(e)}")

    try:
        connection['cursor'].execute(SelectCityData.CITIES.value)
        city_data = [convert_city_response(*row) for row in connection['cursor'].fetchall()][0]

    except Exception as e:
        not_found(f"City id not found by error: {e} - Type: {type(e)}")

    disconnect_to_postgres(connection)

    return jsonify({
        'message': f'Cities successfully created',
        'body': city_data}, 200)


def update_city_into_database(city_id: str, dataset: dict) -> Response:
    """
    Updates a city based on the city_id with the values given in the dataset.
    :param city_id: The uuid from city
    :param dataset: Dict of default information from city. Look to '<repo-root>/README.md' to visit the setup.
                    With updated information.
    :return: City which has been updated into the database
    """
    connection: dict = connect_to_postgres()
    beauty_score: int = get_beauty_score(dataset.get('beauty'))
    city_data: dict = {}

    try:
        connection['cursor'].execute(UpdateCityData.CITY.value, (
            dataset.get('name'),
            dataset.get('geo_location_latitude'),
            dataset.get('geo_location_longitude'),
            beauty_score,
            dataset.get('population'),
            city_id
        ))
        connection['conn'].commit()

        if dataset.get('allied_cities') is not None:
            connection = insert_alliances(connection, dataset.get('allied_cities'), city_id)
        else:
            connection = delete_alliances(connection, city_id)

    except Exception as e:
        conflict(f"City can't be updated by error: {e} - Type: {type(e)}")

    try:
        connection['cursor'].execute(SelectCityData.CITIES.value)
        city_data = [convert_city_response(*row) for row in connection['cursor'].fetchall()][0]

    except Exception as e:
        not_found(f"City id not found by error: {e} - Type: {type(e)}")

    disconnect_to_postgres(connection)

    return jsonify({
        'message': 'City successfully updated',
        'body': city_data}, 200)
