import pytest
import src.reminder as app
from src.reminder import Task


@pytest.mark.parametrize("test_input, expected",
                         [("buy usdt", Task(name="buy usdt")),
                          ("buy solana", None),
                          ("PAY RENT", Task(name="pay rent"))
                          ])
def test_find_task(test_input, expected):
    task_list = [Task(name="pay rent"), Task(name="buy usdt")]
    assert app._find_task(test_input, task_list) == expected
