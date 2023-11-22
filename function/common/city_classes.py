from enum import Enum


class SelectCityData(Enum):
    CITIES = ("SELECT city.city_uuid, city.name, city.geo_location_latitude, city.geo_location_longitude, "
              "bs.description, city.population FROM city "
              "INNER JOIN beauty_score AS bs ON city.beauty = bs.id;")

    CITY = ("SELECT city.city_uuid, city.name, city.geo_location_latitude, city.geo_location_longitude, "
            "bs.description, city.population FROM city "
            "INNER JOIN beauty_score AS bs ON city.beauty = bs.id "
            "WHERE city.city_uuid = %s;")


class DeleteCityData(Enum):
    CITY = ("DELETE FROM alliances WHERE city = %s or allied_cities = %s;"
            "DELETE FROM city WHERE city_uuid = %s;")
