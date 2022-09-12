import reminder as app
from reminder import Task

import pytest


@pytest.mark.parametrize("test_input, expected",
        [("buy bread", Task(name="buy bread")),
         ("buy banana", None),
         ("PAY RENT", Task(name="pay rent")),
         ])
def test_find_task(test_input, expected):
    task_list = [Task(name="pay rent"), Task(name="buy bread")]
    assert app._find_task(test_input, task_list) == expected

