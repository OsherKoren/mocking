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
