import json
from typing import Dict

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


def extract_monthly_adj_close(*, data: dict) -> Dict[str, str]:
    adjusted_close = {}
    for k, v in data.items():
        adjusted_close[k] = v['5. adjusted close']
    return adjusted_close
