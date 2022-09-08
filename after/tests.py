import reminder as app
from reminder import Task

def test_find_task():
    task_list = [Task(name="pay rent"), Task(name="buy bread")]
    assert app._find_task("buy bread", task_list) == Task(name="buy bread")

def test_find_task_none():
    task_list = [Task(name="pay rent"), Task(name="buy bread")]
    assert app._find_task("buy banana", task_list) is None
