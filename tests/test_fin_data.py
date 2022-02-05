import pytest

from data import fin_data


@pytest.fixture()
def mock_requests(requests_mock):
    requests_mock.get(
        url='https://www.alphavantage.co/query',
        json=[
                   {'json': {'fake key': 'fake value'}, 'status_code': 200},
                   {'json': 'Requests status: 404', 'status_code': 404}
               ]
    )


def test_success_requests_monthly_data(mock_requests):
    fst_result = fin_data.requests_monthly_data(symbol='fake_symbol')[0].get('json').get('fake key')
    assert fst_result == 'fake value'


def test_failed_requests_monthly_data(mock_requests):
    status = fin_data.requests_monthly_data(symbol='fake_symbol')[1].get('status_code')
    if status != 200:
        sec_result = fin_data.requests_monthly_data(symbol='fake_symbol')[1].get('json')
    assert sec_result == 'Requests status: 404'


@pytest.fixture
def setup_json():
    returned_json = {"2022-02-03": {"1. open": "241.8000",
                                    "2. high": "246.9700",
                                    "3. low": "228.5100",
                                    "4. close": "231.2000",
                                    "5. adjusted close": "231.2000",
                                    "6. volume": "1857264",
                                    "7. dividend amount": "0.0000"},
                     "2022-01-31": {"1. open": "284.0000",
                                    "2. high": "286.7800",
                                    "3. low": "200.8600",
                                    "4. close": "238.2200",
                                    "5. adjusted close": "238.2200",
                                    "6. volume": "20342202",
                                    "7. dividend amount": "0.0000"},
                     "2021-12-31": {"1. open": "335.0100",
                                    "2. high": "344.7850",
                                    "3. low": "257.3200",
                                    "4. close": "280.5700",
                                    "5. adjusted close": "280.5700",
                                    "6. volume": "25754011",
                                    "7. dividend amount": "0.0000"},
                     "2021-11-30": {"1. open": "360.0000",
                                    "2. high": "389.7100",
                                    "3. low": "324.7300",
                                    "4. close": "327.7600",
                                    "5. adjusted close": "327.7600",
                                    "6. volume": "14278572",
                                    "7. dividend amount": "0.0000"}
                    }
    yield returned_json


@pytest.mark.parametrize('test_key, expected',
                         [
                             ('2022-02-03', '231.2000'),
                             ('2022-01-31', '238.2200'),
                             ('2021-12-31', '280.5700'),
                             ('2021-11-30', '327.7600'),
                         ]
                         )
def test_extract_monthly_adj_close(setup_json, test_key, expected):
    assert fin_data.extract_monthly_adj_close(data=setup_json).get(test_key) == expected
