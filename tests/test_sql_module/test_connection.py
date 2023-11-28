from sql_module.connection import connect_to_postgres, disconnect_to_postgres


def test_connect_to_postgres():
    """
    Test connect to postgres db
    :return: None
    """
    connection_data = connect_to_postgres()
    assert connection_data["conn"] is not None
    assert connection_data["cursor"] is not None
    assert connection_data["conn"].closed == 0
    assert connection_data["cursor"].closed == 0
    connection_data["cursor"].close()
    connection_data["conn"].close()


def test_disconnect_to_postgres():
    """
    Test disconnect from postgres
    :return:
    """
    connection_data = connect_to_postgres()
    disconnect_to_postgres(connection_data)
    assert connection_data["conn"].closed == 1
    assert connection_data["cursor"].closed == 1
