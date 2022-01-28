from configparser import ConfigParser
from pathlib import Path


def get_path(*, file_name: str):
    relative_path = Path(__file__).parent.parent
    path_file = relative_path / file_name
    return path_file


def get_config(*, file_name: str = 'config_file.ini'):
    path_conf_file = get_path(file_name=file_name)
    config = ConfigParser()
    config.read(path_conf_file)
    return config


def get_host():
    config = get_config()
    return config.get('dev', 'HOST')


conf = get_config()
# print(conf)

host = get_host()
# print(host)
