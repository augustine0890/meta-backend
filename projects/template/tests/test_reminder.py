import datetime as dt

import pytest
import src.reminder as app
from src.reminder import Task


def test_to_date():
    assert app._to_date("2023-10-08") == dt.date(2023, 10, 8)


def test_to_date_exception():
    with pytest.raises(ValueError, match="12345 is not in YYYY-MM-DD format."):
        app._to_date("12345")


@pytest.fixture
def task_list():
    return [Task(name="pay rent"), Task(name="buy usdt")]


@pytest.mark.parametrize("test_input, expected",
                         [("buy usdt", Task(name="buy usdt")),
                          ("buy solana", None),
                          ("PAY RENT", Task(name="pay rent"))
                          ])
def test_find_task(test_input, expected, task_list):
    assert app._find_task(test_input, task_list) == expected


def test_save_load_task_list(task_list):
    app._save_task_list(task_list)
    load_list = app._get_task_list()
    assert task_list == load_list
