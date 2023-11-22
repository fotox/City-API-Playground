from common.city_classes import SelectCityData
from sql_module.connection import *


def load_alliances(connection: dict, city_id: str) -> tuple[list, dict]:
    logger.debug(f"Query: {SelectCityData.ALLIANCES.value, (city_id,)}")
    connection['cursor'].execute(SelectCityData.ALLIANCES.value, (city_id,))
    result = [row[0] for row in connection['cursor'].fetchall()]
    logger.debug(f"Result Alliances: {result}")
    return result, connection


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


def load_city(city_id: str = None):
    connection = connect_to_postgres()
    city_list: list = []
    if city_id is None:
        connection['cursor'].execute(SelectCityData.CITIES.value)
        result = [convert_city_response_to_dict(*row) for row in connection['cursor'].fetchall()]
    else:
        connection['cursor'].execute(SelectCityData.CITY.value, (city_id,))
        result = [convert_city_response_to_dict(*row) for row in connection['cursor'].fetchall()]

    for city in result:
        alliances, connection = load_alliances(connection, city['city_uuid'])
        city['allied_cities'] = alliances
        city_list.append(city)

    cancel_connection_to_postgres(connection)
    return city_list
