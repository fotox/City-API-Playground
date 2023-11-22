from enum import Enum


class SelectCityData(Enum):
    CITIES = ("SELECT city.city_uuid, city.name, city.geo_location_latitude, city.geo_location_longitude, "
              "bs.description, city.population FROM city "
              "INNER JOIN beauty_score AS bs ON city.beauty = bs.id;")

    CITY = ("SELECT city.city_uuid, city.name, city.geo_location_latitude, city.geo_location_longitude, "
            "bs.description, city.population FROM city "
            "INNER JOIN beauty_score AS bs ON city.beauty = bs.id "
            "WHERE city.city_uuid = %s;")

    ALLIANCES = ("SELECT allied_cities FROM alliances "
                 "WHERE city = %s;")
