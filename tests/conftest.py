import pytest

API_KEY = 'xxxx'


@pytest.fixture
def mock_get_file_path(monkeypatch):
    # monkeypatch utils.get_file_path as a fixture
    def mock_path(*args, **kwargs):
        return r'C:\fake_folder\fake_sub_folder\fake_file'
    # monkeypatch to replace get_file_path with the behavior of the mock_path defined above
    monkeypatch.setattr('data.utils.get_file_path', mock_path)


@pytest.fixture
def mock_get_config(monkeypatch):
    # monkeypatch utils.get_config as a fixture
    def mock_config(*args, **kwargs):
        return {
                'HOST': 'fake_host_val'
        }
    # monkeypatch to replace get_config with the behavior of the mock_path defined above
    monkeypatch.setattr('data.utils.get_config', mock_config)


@pytest.fixture
def mock_get_section(monkeypatch):
    # monkeypatch utils.get_config()._sections as a fixture
    def mock_section(*args, **kwargs):
        return {
            'driver': 'fake_driver',
            'server': 'fake_server',
            'db': 'fake_db'
        }
    # monkeypatch to replace utils.get_config()._sections with the behavior of the mock_path defined above
    monkeypatch.setattr('utils.get_config()._sections', mock_section)


@pytest.fixture()
def mock_requests(requests_mock):
    # monkeypatch requests.get()
    requests_mock.get(
        url='https://www.alphavantage.co/query',
        json=[
                   {'json': {'fake key': 'fake value'}, 'status_code': 200},
                   {'json': 'Requests status: 404', 'status_code': 404}
               ]
    )


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


@pytest.fixture()
def setup_generator():
    fst_row = ['2022-02-10', 300]
    sec_row = ['2022-01-31', 200]
    thd_row = ['2021-12-31', 100]
    all_rows = [fst_row, sec_row, thd_row]
    generator = (row for row in all_rows)
    return generator
