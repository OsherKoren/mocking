import pytest

import main


@pytest.mark.parametrize('test_level, expected',
                         [
                            (300, '2021-11-30'),
                            (200, '2022-02-03'),
                            (400, False),
                         ]
                         )
def test_run_data_pipeline(monkeypatch, setup_json, test_level, expected):
    monkeypatch.setattr('data.fin_data.load_json', lambda *args, **kwargs: setup_json)
    assert main.run_data_pipeline(level=test_level) == expected
