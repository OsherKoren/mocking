from configparser import ConfigParser
from pathlib import Path


def get_file_path(*, file_name: str) -> Path:
    """ Gets file_name parameter from the user and returns its path
    :param file_name: File name with its extension. Example: 'config_file.ini'
    :return: The path
    """
    relative_path = Path(__file__).parent.parent
    file_path = relative_path / file_name
    return file_path


def get_config(*, file_name: str = 'config_file.ini') -> ConfigParser:
    """ Gets the configparser object
    :param file_name: File name with its extension. Default is set to: 'config_file.ini'
    :return: ConfigParser object
    """
    conf_file_path = get_file_path(file_name=file_name)
    config = ConfigParser()
    config.read(conf_file_path)
    return config


def get_api_key() -> str:
    """ :return: The host from the config file """
    config = get_config()
    return config.get('client', 'API_KEY')


def get_conn_str(*, section: dict = {}) -> str:
    """ Gets the connection file.
    :param section: If the section is set to default: empty dictionary, then gets the section from the config file
    :return: The connection string for connecting to db.
    """
    section = section or get_config()._sections['db']  # pylint: disable=W0212
    driver = section.get('driver')
    server = section.get('server')
    db = section.get('db')
    return f'DRIVER={driver};SERVER={server};DATABASE={db}'
