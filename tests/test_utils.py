from configparser import ConfigParser

from configuration import utils


def test_get_file_path():
    conf_file_path = utils.get_file_path(file_name='config_file.ini')
    assert conf_file_path.is_file()


def test_get_config(monkeypatch):
    # mocked return function to replace utils.get_path by returning 'C:/fake_folder/fake_sub_folder/fake_file'
    def mock_path(*args, **kwargs):
        return r'C:\fake_folder\fake_sub_folder\fake_file'
    # Application of the monkeypatch to replace get_path with the behavior of the mock_path defined above
    monkeypatch.setattr("configuration.utils.get_file_path", mock_path)
    assert isinstance(utils.get_config(file_name='fake_file'), ConfigParser)


def test_get_host(monkeypatch):
    def mock_config():
        return {
                'HOST': 'fake_host_val'
        }
    monkeypatch.setattr("configuration.utils.get_config", mock_config)
    assert utils.get_host() == 'HOST'
