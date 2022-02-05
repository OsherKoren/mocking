# This is the main module for running the fin_data.py script .
from pprint import pprint

from data import fin_data

SYMBOL: str = "SEDG"  # The symbol of the requested stock


if __name__ == '__main__':
    response = fin_data.requests_monthly_data(symbol=SYMBOL)
    if response is not None:
        fin_data.dump_to_json(data=response, file_name=f'{SYMBOL}.json')
    monthly_data = fin_data.load_json(file=f'{SYMBOL}.json')
    adj_close = fin_data.extract_monthly_adj_close(data=monthly_data)
    pprint(adj_close)
