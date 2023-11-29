import os
import pytest

from app import app
from log_module.log_app import viki_log
from sql_module.execution import execute_sql_by_script

logger = viki_log("city_api")
SCRIPT_PATH: str = os.path.dirname(os.path.realpath(__file__))


@pytest.fixture
def test_app():
    with app.app_context():
        yield app


@pytest.fixture(scope="function")
def test_client(test_app):
    execute_sql_by_script(f'{SCRIPT_PATH}\\resources\\0_0_2_init_test_schema.sql')
    execute_sql_by_script(f'{SCRIPT_PATH}\\resources\\0_1_2_import_test_datasets.sql')
    return test_app.test_client()
