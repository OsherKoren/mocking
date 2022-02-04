import requests

from utils import get_api_key


URL = "https://www.alphavantage.co/query"
API_KEY = get_api_key()


def query_monthly_data(*, symbol: str) -> str:
    """ The function requests data via api
    :return: The requested data
    """
    querystring = {"symbol": symbol,
                   "function": "TIME_SERIES_MONTHLY_ADJUSTED",
                   "datatype": "json",
                   "apikey": API_KEY}
    response = requests.get(URL, params=querystring)
    print(type(response.text))
    status = response.status_code
    if status == 200:
        return response.text
    print(f'Requests status: {status}')


data = query_monthly_data(symbol="MSFT")




