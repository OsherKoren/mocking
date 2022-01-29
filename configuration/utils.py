from configparser import ConfigParser
from pathlib import Path

import pyodbc


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
    return config.get('client', 'HOST')


def get_conn_str():
    config = get_config()
    driver = config.get('mssql', 'DRIVER')
    server = config.get('mssql', 'SERVER')
    db = config.get('mssql', 'DB')
    conn = pyodbc.connect(f'DRIVER={driver};SERVER={server};DATABASE={db}')
    return conn


print(get_conn_str())
