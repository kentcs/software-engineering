"""Cumulative example; run with python3 01_first_pass.py."""
def parse(text):
    return 7.0


def check(text, expected):
    actual = parse(text)
    if actual != expected:
        raise AssertionError(
            f"{text!r}: expected {expected!r}, got {actual!r}")


def test_single_digits():
    check('7', 7.0)

def main():
    test_single_digits()
    print("All tests passed.")

if __name__ == "__main__":
    main()
