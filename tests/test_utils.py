from configparser import ConfigParser

import pyodbc
import pytest

from data import utils


def test_get_file_path():
    """ Test get_file_path function """
    conf_file_path = utils.get_file_path(file_name='config_file.ini')
    assert conf_file_path.is_file()


def test_get_config(mock_get_file_path):
    """ Test get_config function """
    assert isinstance(utils.get_config(file_name='fake_file'), ConfigParser)


def test_api_key(mock_get_config):
    """ Test get_host function """
    assert utils.get_api_key() == 'API_KEY'


@pytest.mark.parametrize('test_section, expected_conn_str',
                         [
                             ({}, 'DRIVER={SQL Server};SERVER=.;DATABASE=DEMO'),
                             ({
                                 'driver': 'test_driver',
                                 'server': 'test_server',
                                 'db': 'test_db'
                             }, 'DRIVER=test_driver;SERVER=test_server;DATABASE=test_db'),
                         ]

                         )
def test_get_conn_str(test_section, expected_conn_str):
    """ Test get_conn_str function """
    assert utils.get_conn_str(section=test_section) == expected_conn_str


def test_db_connection():
    """ Test connection to the db """
    test_query = 'SELECT TOP 1 FIRST_NAME FROM EMPLOYEES'
    conn_str = utils.get_conn_str()
    with pyodbc.connect(conn_str) as connector:
        row = connector.execute(test_query).fetchone()
        expected = row[0]
        assert expected == 'Steven'
