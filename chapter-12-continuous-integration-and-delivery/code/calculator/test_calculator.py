"""Examples of agreed calculator behavior, including regression cases."""
import pytest
from calculator import add


@pytest.mark.parametrize("left,right,expected", [
    (2, 2, 4),
    (3, 3, 6),
    (2, 3, 5),
    (3, 2, 5),
    (-2, -3, -5),
    (-2, 3, 1),
    (2, -3, -1),
    (0, 7, 7),
    (7, 0, 7),
])
def test_add(left, right, expected):
    assert add(left, right) == expected


def test_decimal_addition():
    assert add(3.1, 4.2) == pytest.approx(7.3)
