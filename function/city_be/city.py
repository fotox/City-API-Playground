from common.city_classes import SelectCityData
from sql_module.connection import *


def load_all_cities() -> dict:
    connection = connect_to_postgres()
    connection['cursor'].execute(SelectCityData.CITIES.value)
    result = connection['cursor'].fetchall()
    cancel_connection_to_postgres(connection)
    return result


def load_city(city_id: str) -> dict:
    connection = connect_to_postgres()
    connection['cursor'].execute(SelectCityData.CITY.value, (city_id, ))
    result = connection['cursor'].fetchall()
    cancel_connection_to_postgres(connection)
    return result
