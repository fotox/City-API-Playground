import os
from enum import Enum

from dotenv import load_dotenv

load_dotenv()
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

    POPULATION = f"SELECT {SCHEME}.city.population FROM {SCHEME}.city WHERE {SCHEME}.city.city_uuid = %s;"

    LOCATION = (f"SELECT {SCHEME}.city.geo_location_latitude, {SCHEME}.city.geo_location_longitude "
                f"FROM {SCHEME}.city "
                f"WHERE {SCHEME}.city.city_uuid = %s;")


class DeleteCityData(Enum):
    CITY = (f"DELETE FROM {SCHEME}.alliances WHERE {SCHEME}.city = %s or {SCHEME}.allied_cities = %s;"
            f"DELETE FROM {SCHEME}.city WHERE {SCHEME}.city_uuid = %s;")


class InsertCityData(Enum):
    CITY = (f"INSERT INTO {SCHEME}.city (city_uuid, name, geo_location_latitude, geo_location_longitude, "
            f"beauty, population) "
            f"VALUES (%s, %s, %s, %s, %s, %s)")


class UpdateCityData(Enum):
    CITY = (f"UPDATE {SCHEME}.city "
            f"SET name = %s, geo_location_latitude = %s, geo_location_longitude = %s, beauty = %s, population = %s "
            f"WHERE {SCHEME}.city.city_uuid = %s")
