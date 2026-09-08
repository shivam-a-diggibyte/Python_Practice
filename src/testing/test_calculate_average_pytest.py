# test_calculate_average_pytest.py

import pytest
from calculate_average import calculate_average

def test_normal_case():
    assert calculate_average([80, 90, 70]) == 80

def test_raises_on_empty_list():
    with pytest.raises(ZeroDivisionError):
        calculate_average([])

@pytest.mark.parametrize("marks, expected", [ # pytest paramertrization
    ([80, 90, 70], 80),
    ([100], 100),
    ([50, 50], 50),
])
def test_calculate_average_parametrized(marks, expected):
    assert calculate_average(marks) == expected
