import pytest

from app import app
from sql_module.execution import execute_sql_by_script


@pytest.fixture
def test_app():
    with app.app_context():
        yield app


@pytest.fixture(scope="function")
def test_client(test_app):
    execute_sql_by_script('function/sql_module/resources/0_0_2_init_test_schema.sql')
    execute_sql_by_script('function/sql_module/resources/0_1_2_import_test_datasets.sql')
    return test_app.test_client()
