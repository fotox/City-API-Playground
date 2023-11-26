from enum import Enum


class SelectBeautyData(Enum):
    BEAUTY_NAME = "SELECT * FROM beauty_score;"

    BEAUTY_SCORE_BY_NAME = "SELECT id FROM beauty_score WHERE description LIKE %s;"

    BEAUTY_NAME_BY_SCORE = "SELECT description FROM beauty_score WHERE id = %s;"
