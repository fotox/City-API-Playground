import uuid

from flask import jsonify, Response, abort

from common.alliances_classes import *
from common.beauty_score_classes import *
from common.city_classes import *
from sql_module.connection import *
from log_module.log_app import viki_log

logger = viki_log("city_api")


def load_alliances(connection: dict, city_id: str) -> tuple[list, dict]:
    connection['cursor'].execute(SelectAlliancesData.ALLIANCES.value, (city_id,))
    result = [row[0] for row in connection['cursor'].fetchall()]
    return result, connection


def get_beauty_score(beauty: str | int) -> int | str:
    connection = connect_to_postgres()

    try:
        beauty_score: int = connection['cursor'].execute(SelectBeautyData.BEAUTY_SCORE_BY_NAME.value, (beauty,))
    except Exception as e:
        abort(500, description=f'Random Message - TODO. {str(e)}')

    finally:
        disconnect_to_postgres(connection)

    return beauty_score


def convert_city_response_to_dict(city_uuid: str, name: str, geo_location_latitude: float,
                                  geo_location_longitude: float, beauty: str, population: int) -> dict:
    return {
        'city_uuid': city_uuid,
        'name': name,
        'geo_location_latitude': geo_location_latitude,
        'geo_location_longitude': geo_location_longitude,
        'beauty': beauty,
        'population': population,
        'allied_cities': []
    }


def get_city_from_database(city_id: str = None) -> list:
    connection = connect_to_postgres()
    city_list: list = []

    try:
        if city_id is None:
            connection['cursor'].execute(SelectCityData.CITIES.value)
            result = [convert_city_response_to_dict(*row) for row in connection['cursor'].fetchall()]
        else:
            connection['cursor'].execute(SelectCityData.CITY.value, (city_id,))
            result = [convert_city_response_to_dict(*row) for row in connection['cursor'].fetchall()]

    except Exception as e:
        abort(500, description=f'Random Message - TODO. {str(e)}')

    finally:
        disconnect_to_postgres(connection)

    for city in result:
        alliances, connection = load_alliances(connection, city['city_uuid'])
        city['allied_cities'] = alliances
        city_list.append(city)

    return city_list


def delete_city_from_database(city_id: str) -> Response:
    connection = connect_to_postgres()
    try:
        connection['cursor'].execute(DeleteCityData.CITY.value, (city_id,))

    except Exception as e:
        abort(500, description=f'Random Message - TODO. {str(e)}')

    finally:
        disconnect_to_postgres(connection)

    return jsonify({'message': 'Item deleted successfully'})


def insert_city_into_database(dataset: dict) -> Response:
    connection = connect_to_postgres()
    beauty_score = get_beauty_score(dataset.get('beauty'))
    city_gen_uuid: str = str(uuid.uuid4())
    logger.debug(f"Beauty Score is {beauty_score}")
    try:
        connection['cursor'].execute(InsertCityData.CITY.value, (
            city_gen_uuid,
            dataset.get('name'),
            dataset.get('geo_location_latitude'),
            dataset.get('geo_location_longitude'),
            beauty_score,
            dataset.get('population')
        ))

        for alliance_city in dataset.get('allied_cities'):
            connection['cursor'].execute(InsertAllianceData.ALLIANCES.value, (
                city_gen_uuid,
                alliance_city
            ))

        connection['conn'].commit()
        result = jsonify({'message': 'Item created successfully'})

    except Exception as e:
        abort(500, description=f'Random Message - TODO. {str(e)}')

    finally:
        disconnect_to_postgres(connection)

    return result


def insert_alliances_to_city(dataset: dict) -> Response:
    connection = connect_to_postgres()
    try:
        connection['cursor'].execute(InsertAllianceData.ALLIANCES.value, (
            dataset['city_id'],
            dataset['alliances_city_id'],
        ))
        connection['conn'].commit()
        result = jsonify({'message': 'Alliance between cities updated successfully'})

    except Exception as e:
        abort(500, description=f'Random Message - TODO. {str(e)}')

    finally:
        disconnect_to_postgres(connection)

    return result


def update_city_into_database(dataset: dict) -> Response:
    connection = connect_to_postgres()
    beauty_score = get_beauty_score(dataset.get('beauty'))
    logger.debug(f"Beauty Score is {beauty_score}")

    try:
        connection['cursor'].execute(UpdateCityData.CITY.value, (
            dataset.get('name'),
            dataset.get('geo_location_latitude'),
            dataset.get('geo_location_longitude'),
            beauty_score,
            dataset.get('population'),
            dataset.get('city_uuid'),
        ))
        connection['conn'].commit()
        disconnect_to_postgres(connection)
        result = jsonify({'message': 'City updated successfully'})

    except Exception as e:
        abort(500, description=f'Random Message - TODO. {str(e)}')

    finally:
        disconnect_to_postgres(connection)

    return result
