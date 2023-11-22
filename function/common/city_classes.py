from enum import Enum


class SelectCityData(Enum):
    CITIES = ("SELECT * FROM city "
              "INNER JOIN beauty_score ON city.beauty = beauty_score.id ")

    CITY = ("SELECT * FROM city "
            "INNER JOIN beauty_score ON city.beauty = beauty_score.id "
            "WHERE city_uuid = %s;")
