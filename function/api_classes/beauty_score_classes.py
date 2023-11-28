import os
from enum import Enum

from dotenv import load_dotenv

load_dotenv()
SCHEME = os.getenv('PGSCHEME')


class SelectBeautyData(Enum):
    BEAUTY_NAME = f"SELECT * FROM {SCHEME}.beauty_score;"

    BEAUTY_SCORE_BY_NAME = (f"SELECT {SCHEME}.beauty_score.id "
                            f"FROM {SCHEME}.beauty_score "
                            f"WHERE {SCHEME}.beauty_score.description LIKE %s;")

    BEAUTY_NAME_BY_SCORE = (f"SELECT {SCHEME}.beauty_score.description "
                            f"FROM {SCHEME}.beauty_score "
                            f"WHERE {SCHEME}.beauty_score.id = %s;")
