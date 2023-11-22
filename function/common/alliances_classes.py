from enum import Enum


class SelectAlliancesData(Enum):
    ALLIANCES = ("SELECT allied_cities FROM alliances "
                 "WHERE city = %s;")


class InsertAllianceData(Enum):
    ALLIANCES = ("INSERT INTO alliances"
                 "")
