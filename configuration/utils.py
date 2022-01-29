from configparser import ConfigParser
from ctypes import Union
from pathlib import Path


def get_file_path(*, file_name: str) -> Path:
    relative_path = Path(__file__).parent.parent
    file_path = relative_path / file_name
    return file_path


def get_config(*, file_name: str = 'config_file.ini') -> ConfigParser:
    conf_file_path = get_file_path(file_name=file_name)
    config = ConfigParser()
    config.read(conf_file_path)
    return config


def get_host() -> str:
    config = get_config()
    return config.get('dev', 'HOST')


conf = get_config()
print(conf)

host = get_host()
print(host)
