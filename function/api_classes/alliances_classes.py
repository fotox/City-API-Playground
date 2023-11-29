import os
from enum import Enum

SCHEME = os.environ['PGSCHEME']


class SelectAlliancesData(Enum):
    ALLIANCES = (f"SELECT {SCHEME}.alliances.allied_cities FROM {SCHEME}.alliances "
                 f"WHERE {SCHEME}.alliances.city = %s;")


class InsertAllianceData(Enum):
    ALLIANCES = (f"INSERT INTO {SCHEME}.alliances (city, allied_cities) "
                 f"VALUES (%s, %s);")


class DeleteAllianceData(Enum):
    ALLIANCES = (f"DELETE FROM {SCHEME}.alliances "
                 f"WHERE city = %s or allied_cities = %s;")
