"""Testing-agency exercise. Change the imported version as the suite grows.

Run without Python's -O option so assertions execute.
The supplied versions are intentionally incorrect.
"""
from maths import add1 as add


def test_two_plus_two():
    assert add(2, 2) == 4


def test_another_equal_pair():
    assert add(3, 3) == 6


def test_larger_equal_pair():
    assert add(4, 4) == 8


def test_unequal_positive_values():
    assert add(2, 3) == 5
    assert add(3, 2) == 5


def test_negative_values():
    assert add(-2, -3) == -5
    assert add(-2, 3) == 1
    assert add(2, -3) == -1


def test_zero_and_fractions():
    assert add(0, 0) == 0
    assert add(0, 7) == 7
    assert add(7, 0) == 7
    assert add(0.25, 0.5) == 0.75
    assert add(-0.25, 0.5) == 0.25


def main():
    test_two_plus_two()
    test_another_equal_pair()
    test_larger_equal_pair()
    test_unequal_positive_values()
    test_negative_values()
    test_zero_and_fractions()
    print("All agency tests passed.")


if __name__ == "__main__":
    main()
