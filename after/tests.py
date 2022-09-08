import reminder as app
from reminder import Task

def test_find_task():
    tast_list = [Task(name="pay rent"), Task(name="buy bread")]
    assert app._find_task("buy bread", tast_list) == Task(name="buy bread")

def test_find_task_none():
    tast_list = [Task(name="pay rent"), Task(name="buy bread")]
    assert app._find_task("buy banana", tast_list) is None
