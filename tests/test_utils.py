from configparser import ConfigParser

from configuration import utils


def test_get_file_path():
    conf_file_path = utils.get_file_path(file_name='config_file.ini')
    assert conf_file_path.is_file()


def test_get_config(mock_get_file_path):
    assert isinstance(utils.get_config(file_name='fake_file'), ConfigParser)


def test_get_host(mock_get_config):
    assert utils.get_host() == 'HOST'
