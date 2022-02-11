# This is the main module for running the fin_data.py script .
from typing import Union

from data import fin_data


# Set the constant variables before running the module
SYMBOL: str = "SEDG"  # The symbol of the requested stock
LEVEL: int = 300  # The level of the stock price that the user wants to be alerted for
WEB_DATA: bool = False  # Get new monthly data from the web.


def run_data_pipeline(*, level: int = LEVEL, web_data: bool = WEB_DATA) -> Union[str, bool]:
    """ Main function - runs functions to extract, load and transform the data
    :param level: The level of the stock price that the user wants to check
    :param web_data: If set to True, the program will extract new monthly data from the web.
    :return: An alert if the price reached the level, False if not
    """
    if web_data:
        response = fin_data.requests_monthly_data(symbol=SYMBOL)
        if response is not None:
            fin_data.dump_to_json(data=response, file_name=f'{SYMBOL}.json')
    monthly_data = fin_data.load_json(file=f'{SYMBOL}.json')
    numeric_monthly_data = fin_data.convert_values_into_float(dic=monthly_data)
    adj_close = fin_data.extract_monthly_adj_close_as_a_generator(data=numeric_monthly_data)
    level_alert = fin_data.check_price_level(data=adj_close, level=level)
    return level_alert


if __name__ == '__main__':
    alert = run_data_pipeline()
    if alert:
        print(f'The stock reached the level price on {alert} ')
    else:
        print("The stock didn't reach the level price ")

