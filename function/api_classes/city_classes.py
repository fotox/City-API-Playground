import os
from enum import Enum

SCHEME = os.getenv('PGSCHEME')


class SelectCityData(Enum):
    CITIES = (f"SELECT {SCHEME}.city.city_uuid, {SCHEME}.city.name, {SCHEME}.city.geo_location_latitude, "
              f"{SCHEME}.city.geo_location_longitude, {SCHEME}.beauty_score.description, {SCHEME}.city.population "
              f"FROM {SCHEME}.city "
              f"INNER JOIN {SCHEME}.beauty_score ON {SCHEME}.city.beauty = {SCHEME}.beauty_score.id;")

    CITY = (f"SELECT {SCHEME}.city.city_uuid, {SCHEME}.city.name, {SCHEME}.city.geo_location_latitude, "
            f"{SCHEME}.city.geo_location_longitude, {SCHEME}.beauty_score.description, {SCHEME}.city.population "
            f"FROM {SCHEME}.city "
            f"INNER JOIN {SCHEME}.beauty_score ON {SCHEME}.city.beauty = {SCHEME}.beauty_score.id "
            f"WHERE {SCHEME}.city.city_uuid = %s;")

    POPULATION = f"SELECT {SCHEME}.population FROM {SCHEME}.city WHERE {SCHEME}.city_uuid = %s;"

    LOCATION = (f"SELECT {SCHEME}.geo_location_latitude, {SCHEME}.geo_location_longitude "
                f"FROM {SCHEME}.city "
                f"WHERE {SCHEME}.city_uuid = %s;")


class DeleteCityData(Enum):
    CITY = (f"DELETE FROM {SCHEME}.alliances WHERE {SCHEME}.city = %s or {SCHEME}.allied_cities = %s;"
            f"DELETE FROM {SCHEME}.city WHERE {SCHEME}.city_uuid = %s;")


class InsertCityData(Enum):
    CITY = (f"INSERT INTO {SCHEME}.city ({SCHEME}.city_uuid, {SCHEME}.name, {SCHEME}.geo_location_latitude, "
            f"{SCHEME}.geo_location_longitude, {SCHEME}.beauty, {SCHEME}.population) "
            f"VALUES (%s, %s, %s, %s, %s, %s)")


class UpdateCityData(Enum):
    CITY = (f"UPDATE {SCHEME}.city "
            f"SET {SCHEME}.name = %s, {SCHEME}.geo_location_latitude = %s, {SCHEME}.geo_location_longitude = %s, "
            f"{SCHEME}.beauty = %s, {SCHEME}.population = %s "
            f"WHERE {SCHEME}.city_uuid = %s")
