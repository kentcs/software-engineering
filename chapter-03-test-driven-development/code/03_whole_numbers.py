"""Cumulative example; run with python3 03_whole_numbers.py."""
def parse(text):
    value = 0.0
    for digit in text:
        value = value * 10 + ord(digit) - ord("0")
    return value


def check(text, expected):
    actual = parse(text)
    if actual != expected:
        raise AssertionError(
            f"{text!r}: expected {expected!r}, got {actual!r}")


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

def main():
    test_single_digits()
    test_multiple_digits()
    print("All tests passed.")

if __name__ == "__main__":
    main()
