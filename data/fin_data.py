import json
from typing import Dict, Generator, List

import requests

from data import utils


URL = 'https://www.alphavantage.co/query'
API_KEY = utils.get_api_key()


def requests_monthly_data(*, symbol: str) -> Dict[str, str]:
    """ The function requests data via api
    :return: The requested data in a dictionary format
    """
    querystring = {"symbol": symbol,
                   "function": "TIME_SERIES_MONTHLY_ADJUSTED",
                   "apikey": API_KEY}
    response = requests.get(URL, params=querystring)
    status = response.status_code
    if status == 200:
        return response.json()
    print(f'Requests status: {status}')


def dump_to_json(*, data: Dict, file_name: str) -> bool:
    """ Save the data into a json file
    :param data: The data
    :param file_name: The file name to be saved as.
    :return: An indication of success
    """
    with open(file_name, 'w') as file:
        json.dump(data, file)
        return True
    return False


def load_json(*, file: str) -> Dict[str, str]:
    """ The function opens a JSON file and returns the monthly data as a dictionary
    :param: file: Json file to read data from
    :return: A dictionary with the date as the key and the adjusted close price as the value
    """
    with open(file) as json_file:
        all_data = json.load(json_file)
    return all_data['Monthly Adjusted Time Series']


def convert_values_into_float(*, dic: Dict):
    """ Convert the numeric values inside the nested dictionary from string type into float type
    :param dic: A nested dictionary
    :return: A nested dictionary with inner values as float
    """
    return {k: {kk: float(vv) for kk, vv in v.items()} for k, v in dic.items()}


def extract_monthly_adj_close(*, data: dict) -> Dict[str, str]:
    """ Extract the monthly data adjusted close price
    :param data: A dictionary of all data
    :return: A dictionary of only the month as the key and the adjusted price as the value
    """
    adjusted_close = {}
    for k, v in data.items():
        adjusted_close[k] = v['5. adjusted close']
    return adjusted_close


def extract_monthly_adj_close_as_a_generator(*, data: dict) -> Generator[List[str], None, None]:
    """ Extract the monthly data adjusted close price
    :param data: A dictionary of all data
    :return: A dictionary of only the month as the key and the adjusted price as the value
    """
    adjusted_close = []
    for k, v in data.items():
        adjusted_close.append([k, v['5. adjusted close']])
    adjusted_close_generator = (row for row in adjusted_close)
    return adjusted_close_generator


def check_price_level(*, data: Generator, level: float, periods: int = 12) -> bool:
    """ The function checks if the adjusted price reached a specific level in the last 12 months
    :param data: The data of the stock price as a generator type
    :param level: Price level set as a parameter by the user.
    :param periods: Number of periods to check
    :return: True if the price reached the level, False if not.
    """
    try:
        for _period in range(periods):
            row = next(data)
            month = row[0]
            adj_close = row[1]
            if adj_close >= level:
                return month
    except StopIteration:
        return False
