import pytest

from data import fin_data


def test_success_requests_monthly_data(mock_requests):
    fst_result = fin_data.requests_monthly_data(symbol='fake_symbol')[0].get('json').get('fake key')
    assert fst_result == 'fake value'


def test_failed_requests_monthly_data(mock_requests):
    status = fin_data.requests_monthly_data(symbol='fake_symbol')[1].get('status_code')
    if status != 200:
        sec_result = fin_data.requests_monthly_data(symbol='fake_symbol')[1].get('json')
    assert sec_result == 'Requests status: 404'


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


def test_convert_values_into_float(setup_json):
    result = fin_data.convert_values_into_float(dic=setup_json)
    test_values = list(result['2022-02-03'].values())
    for val in test_values:
        assert isinstance(val, float)


@pytest.mark.parametrize('test_level, expected',
                         [
                            (300, '2022-02-10'),
                            (200, '2022-02-10'),
                            (400, False),
                         ]
                         )
def test_check_price_level(setup_generator, test_level, expected):
    assert fin_data.check_price_level(data=setup_generator, level=test_level) == expected
