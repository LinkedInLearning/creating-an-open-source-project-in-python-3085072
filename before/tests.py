import reminder as app
from reminder import Task

import datetime as dt

import pytest

def test_to_date():
    assert app._to_date("2022-09-01") == dt.date(2022, 9, 1)

def test_to_date_exception():
    with pytest.raises(ValueError, match="12345 is not in YYYY-MM-DD format."):
        app._to_date("12345")

@pytest.mark.parametrize("test_input, expected",
        [("buy bread", Task(name="buy bread")),
         ("buy banana", None),
         ("PAY RENT", Task(name="pay rent")),
         ])
def test_find_task(test_input, expected):
    task_list = [Task(name="pay rent"), Task(name="buy bread")]
    assert app._find_task(test_input, task_list) == expected

