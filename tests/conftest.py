import pytest


@pytest.fixture
def mock_get_file_path(monkeypatch):
    # monkeypatch utils.get_file_path as a fixture
    def mock_path(*args, **kwargs):
        return r'C:\fake_folder\fake_sub_folder\fake_file'
    # monkeypatch to replace get_file_path with the behavior of the mock_path defined above
    monkeypatch.setattr("configuration.utils.get_file_path", mock_path)


@pytest.fixture
def mock_get_config(monkeypatch):
    # monkeypatch utils.get_config as a fixture
    def mock_config(*args, **kwargs):
        return {
                'HOST': 'fake_host_val'
        }
    # monkeypatch to replace get_config with the behavior of the mock_path defined above
    monkeypatch.setattr("configuration.utils.get_config", mock_config)


