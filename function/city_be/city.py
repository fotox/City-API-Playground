from common.city_classes import SelectCityData
from sql_module.connection import *


def get_beauty_score():
    # TODO: Load from Database
    return {1: "Ugly", 2: "Average", 3: "Gorgeous"}


def to_dict(city_uuid: str, name: str, geo_location_latitude: float, geo_location_longitude: float, beauty: str,
            population: int) -> dict:
    return {
        'city_uuid': city_uuid,
        'name': name,
        'geo_location_latitude': geo_location_latitude,
        'geo_location_longitude': geo_location_longitude,
        'beauty': beauty,
        'population': population,
        'allied_cities': []
    }


def load_city(city_id: str = None) -> dict:
    connection = connect_to_postgres()
    if city_id is None:
        connection['cursor'].execute(SelectCityData.CITIES.value)
        result = [to_dict(*row) for row in connection['cursor'].fetchall()]
    else:
        connection['cursor'].execute(SelectCityData.CITY.value, (city_id,))
        result = [to_dict(*row) for row in connection['cursor'].fetchall()][0]

    cancel_connection_to_postgres(connection)
    return result
