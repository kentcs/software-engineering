"""Cumulative example; run with python3 04_decimals.py."""
import math


def parse(text):
    value = 0.0
    place = 0.1
    after_point = False
    for digit in text:
        if digit == ".":
            after_point = True
        elif after_point:
            value += (ord(digit) - ord("0")) * place
            place /= 10
        else:
            value = value * 10 + ord(digit) - ord("0")
    return value


def check(text, expected):
    actual = parse(text)
    if not math.isclose(actual, expected, rel_tol=1e-12, abs_tol=1e-12):
        raise AssertionError(
            f"{text!r}: expected {expected!r}, got {actual!r}")


def check_rejected(text):
    try:
        parse(text)
    except ValueError:
        return
    raise AssertionError(f"{text!r}: expected ValueError")


def test_single_digits():
    check('7', 7.0)
    check('0', 0.0)
    check('3', 3.0)
    check('9', 9.0)

def test_multiple_digits():
    check('42', 42.0)
    check('10', 10.0)
    check('105', 105.0)
    check('007', 7.0)

def test_decimal_numbers():
    check('12.5', 12.5)
    check('0.25', 0.25)
    check('12.34', 12.34)
    check('10.02', 10.02)

def main():
    test_single_digits()
    test_multiple_digits()
    test_decimal_numbers()
    print("All tests passed.")

if __name__ == "__main__":
    main()
