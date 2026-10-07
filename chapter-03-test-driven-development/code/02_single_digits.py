"""Cumulative example; run with python3 02_single_digits.py."""
def parse(text):
    return float(ord(text[0]) - ord("0"))


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

def main():
    test_single_digits()
    print("All tests passed.")

if __name__ == "__main__":
    main()
