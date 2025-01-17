from geopy.distance import geodesic

from api_classes.city_classes import SelectCityData

from log_module.log_app import viki_log
logger = viki_log("city_api")


def convert_city_response(city_uuid: str, name: str, geo_location_latitude: float,
                          geo_location_longitude: float, beauty: str, population: int) -> dict:
    """
    Takes the information returned by the database and formats it into the city data record
    :param city_uuid: The uuid from city
    :param name: The name of the city
    :param geo_location_latitude: geo information of latitude
    :param geo_location_longitude: geo information of longitude
    :param beauty: beauty code of the city
    :param population: Number of inhabitants of the city
    :return: formatted city dataset
    """
    return {
        'city_uuid': city_uuid,
        'name': name,
        'geo_location_latitude': geo_location_latitude,
        'geo_location_longitude': geo_location_longitude,
        'beauty': beauty,
        'population': population,
        'allied_cities': []
    }


def calculate_allied_power(connection: dict, city_id: str, latitude: float, longitude: float, alliances: list) -> int:
    """
    Calculates the allied power of a city in relation to the population of that city and the population of allied
    cities in relation to the distance to the allied cities
    :param connection: Open database connection
    :param city_id: The uuid from city
    :param latitude: geo information of latitude
    :param longitude: geo information of longitude
    :param alliances: List of allied cities
    :return: Calculated allied power
    """
    allied_power: int = 0

    try:
        connection['cursor'].execute(SelectCityData.POPULATION.value, (city_id,))
        allied_power = connection['cursor'].fetchall()[0][0]

    except Exception as e:
        logger.error(f"Loading the population of the city from the database failed by error: {e} - Type: {type(e)}")

    if alliances:
        try:
            for alliance_city in alliances:
                connection['cursor'].execute(SelectCityData.POPULATION.value, (alliance_city,))
                population: int = connection['cursor'].fetchall()[0][0]
                connection['cursor'].execute(SelectCityData.LOCATION.value, (alliance_city,))
                location: list = [row for row in connection['cursor'].fetchall()]

                distance: geodesic = calculate_distance((latitude, longitude), location[0])
                if distance < 1000:
                    allied_power += population
                elif distance in range(1000, 10000):
                    allied_power += int(round(population / 2, 0))
                else:
                    allied_power += int(round(population / 4, 0))

        except Exception as e:
            logger.error(f"The calculation of the allied power of the city in connection with loading the distance to "
                         f"the partner city from the database failed by error: {e} - Type: {type(e)}")

    return allied_power


def calculate_distance(source: tuple, destination: tuple) -> geodesic:
    """
    Calculating the distance between two allied cities
    :param source: Coordinates of the capital
    :param destination: Coordinates of the allied city
    :return: Distance in kilometers between the two coordinates
    """
    from geopy.distance import distance
    return distance(source, destination)
