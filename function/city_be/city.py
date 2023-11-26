import uuid

from flask import abort

from common.beauty_score_classes import *
from common.city_classes import *
from common.handler import *
from sql_module.connection import *
from log_module.log_app import viki_log

logger = viki_log("city_api")


def get_beauty_score(beauty: str | int) -> int | str:
    """
    Look into the database table beauty_score and to find a mat
    :param beauty:
    :return:
    """
    connection = connect_to_postgres()
    beauty_score: int = 0

    try:
        if isinstance(beauty, str):
            connection['cursor'].execute(SelectBeautyData.BEAUTY_SCORE_BY_NAME.value, (beauty,))
        else:
            connection['cursor'].execute(SelectBeautyData.BEAUTY_NAME_BY_SCORE.value, (beauty,))
            _beauty_name: str = connection['cursor'].fetchall()[0]
            beauty_score = beauty

    except Exception as e:
        logger.error(f"Beauty code or name not found by error: {e}")

    finally:
        disconnect_to_postgres(connection)

    return beauty_score


def get_city_from_database(city_id: str = None) -> Response:
    connection = connect_to_postgres()
    city_list: list = []
    city_data: list = []

    try:
        if city_id is None:
            connection['cursor'].execute(SelectCityData.CITIES.value)
            city_data = [convert_response(*row) for row in connection['cursor'].fetchall()]
        else:
            connection['cursor'].execute(SelectCityData.CITY.value, (city_id,))
            city_data = [convert_response(*row) for row in connection['cursor'].fetchall()]
            connection['cursor'].execute(SelectAlliancesData.ALLIANCES.value, (city_id,))
            alliances = [row[0] for row in connection['cursor'].fetchall()]
            city_data[0]['allied_power'] = calculate_allied_power(connection,
                                                                  city_id,
                                                                  city_data[0]['geo_location_latitude'],
                                                                  city_data[0]['geo_location_longitude'],
                                                                  alliances)

    except Exception as e:
        not_found(f"City not found by: {e}")

    for city in city_data:
        alliances, connection = load_alliances(connection, city['city_uuid'])
        city['allied_cities'] = alliances
        city_list.append(city)

    disconnect_to_postgres(connection)

    return jsonify({
        'message': 'Cities found successfully',
        'body': city_list}, 200)


def delete_city_from_database(city_id: str) -> Response:
    connection = connect_to_postgres()
    try:
        connection['cursor'].execute(DeleteCityData.CITY.value, (city_id, city_id, city_id,))
        connection['conn'].commit()

    except Exception as e:
        abort(500, description=f'Random Message - TODO. {str(e)}')

    disconnect_to_postgres(connection)

    return jsonify({'message': 'Item deleted successfully'})


def insert_city_into_database(dataset: dict) -> tuple[list, str]:
    connection = connect_to_postgres()
    beauty_score = get_beauty_score(dataset.get('beauty'))
    city_gen_uuid: str = str(uuid.uuid4())

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
        message: str = 'Item created successfully'

    except Exception as e:
        abort(500, description=f'Random Message - TODO. {str(e)}')

    try:
        dataset: list = get_city_from_database(city_gen_uuid)
        logger.debug(dataset)

    except Exception as e:
        logger.error(f"dataset: list = get_city_from_database(city_gen_uuid): {e}")

    disconnect_to_postgres(connection)

    return dataset, message


def update_city_into_database(city_id: str, dataset: dict) -> Response:
    connection = connect_to_postgres()
    beauty_score = get_beauty_score(dataset.get('beauty'))

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

        disconnect_to_postgres(connection)
        result = jsonify({'message': 'City updated successfully'})

    except Exception as e:
        abort(500, description=f'Random Message - TODO. {str(e)}')

    disconnect_to_postgres(connection)

    return result
