import os
import datetime
import pytest
from unittest.mock import patch, MagicMock
from log_module.log_app import viki_log


@pytest.fixture
def mock_zipfile():
    with patch("log_module.log_app.zipfile.ZipFile") as mock:
        yield mock


@pytest.fixture
def mock_remove():
    with patch("log_module.log_app.os.remove") as mock:
        yield mock


@pytest.fixture
def mock_getsize():
    with patch("log_module.log_app.os.path.getsize") as mock:
        yield mock


def test_rollover_and_archive(mock_remove, mock_getsize, mock_zipfile):
    # Mock the write method of ZipFile
    write_mock = MagicMock()
    mock_zipfile.return_value.__enter__.return_value.write = write_mock

    # Mock the getsize method of os.path.path
    mock_getsize.return_value = 100

    with patch("log_module.log_app.TimedRotatingFileHandler.shouldRollover", return_value=True):
        logger = viki_log("test_module")

    assert logger.hasHandlers()  # Check if handler is added

    # Simulate log rollover
    with patch("log_module.log_app.os.path.getsize", return_value=100):
        logger.debug("New log entry")

    # Check if archive and remove were called
    yesterday_date = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y%m%d")
    zip_filename = os.path.abspath(
        f"{os.path.dirname(os.path.realpath(__file__))}"
        f"\\..\\..\\function\\log_module\\archive\\test_module_logs\\test_module_log_{yesterday_date}.zip"
    )

    mock_zipfile.assert_called_once_with(zip_filename, 'w')
    write_mock.assert_called_once_with(
        os.path.abspath(
            f"{os.path.dirname(os.path.realpath(__file__))}"
            f"\\..\\..\\function\\log_module\\current\\test_module.log"
        ),
        "test_module.log"
    )
    mock_remove.assert_called_once_with(
        os.path.abspath(
            f"{os.path.dirname(os.path.realpath(__file__))}"
            f"\\..\\..\\function\\log_module\\current\\test_module.log"
        )
    )


@patch("log_module.log_app.os.path.getsize", return_value=0)
@patch("log_module.log_app.os.remove")
def test_no_rollover_if_empty_log(mock_remove, mock_getsize, mock_zipfile):
    with patch("log_module.log_app.TimedRotatingFileHandler.shouldRollover", return_value=True):
        logger = viki_log("test_module")

    assert logger.hasHandlers()  # Check if handler is added

    # Simulate log rollover
    with patch("log_module.log_app.os.path.getsize", return_value=0):
        logger.debug("New log entry")

    # Ensure that archive and remove were not called
    mock_zipfile.assert_not_called()
    mock_remove.assert_not_called()
