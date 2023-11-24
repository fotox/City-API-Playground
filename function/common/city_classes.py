from enum import Enum


class SelectCityData(Enum):
    CITIES = ("SELECT city.city_uuid, city.name, city.geo_location_latitude, city.geo_location_longitude, "
              "bs.description, city.population FROM city "
              "INNER JOIN beauty_score AS bs ON city.beauty = bs.id;")

    CITY = ("SELECT city.city_uuid, city.name, city.geo_location_latitude, city.geo_location_longitude, "
            "bs.description, city.population FROM city "
            "INNER JOIN beauty_score AS bs ON city.beauty = bs.id "
            "WHERE city.city_uuid = %s;")

    POPULATION = "SELECT population FROM city WHERE city_uuid = %s;"

    LOCATION = "SELECT geo_location_longitude, geo_location_latitude FROM city WHERE city_uuid = %s;"


class DeleteCityData(Enum):
    CITY = ("DELETE FROM alliances WHERE city = %s or allied_cities = %s;"
            "DELETE FROM city WHERE city_uuid = %s;")


class InsertCityData(Enum):
    CITY = ("INSERT INTO city (city_uuid, name, geo_location_latitude, geo_location_longitude, beauty, population) "
            "VALUES (%s, %s, %s, %s, %s, %s)")


class UpdateCityData(Enum):
    CITY = ("UPDATE city "
            "SET name = %s, geo_location_latitude = %s, geo_location_longitude = %s, beauty = %s, population = %s "
            "WHERE city_uuid = %s")
