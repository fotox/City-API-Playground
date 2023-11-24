from enum import Enum


class SelectAlliancesData(Enum):
    ALLIANCES = ("SELECT allied_cities FROM alliances "
                 "WHERE city = %s;")


class InsertAllianceData(Enum):
    ALLIANCES = ("INSERT INTO alliances (city, allied_cities) "
                 "VALUES (%s, %s);")


class DeleteAllianceData(Enum):
    ALLIANCES = "DELETE FROM alliances WHERE city = %s or allied_cities = %s;"
