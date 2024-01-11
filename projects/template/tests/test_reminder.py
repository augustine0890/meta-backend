import src.reminder as app
from src.reminder import Task


def test_find_task():
    task_list = [Task(name="pay rent"), Task(name="buy usdt")]
    assert app._find_task("buy usdt", task_list) == Task(name="buy usdt")
    assert app._find_task("buy usdt", task_list) != Task(name="pay rent")


def test_none_find_task():
    task_list = [Task(name="pay rent"), Task(name="buy usdt")]
    assert app._find_task("buy btc", task_list) == None
