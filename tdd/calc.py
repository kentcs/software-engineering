def parse(s): # --> n
    sign = 1
    if s[0] == "-":
        sign = -1
        s = s[1:]
    n = 0
    d = 1.0
    for c in s:
        if c == ".":
            assert d == 1.0
            d = d / 10
            continue
        assert c in "0123456789"
        if d == 1.0:
            n = n * 10 + ord(c) - ord("0")
        else:
            n = n + (ord(c) - ord("0")) * d
            d = d / 10
    return n * sign

def test_single_digits():
    """ test single digits """
    print("test single digits...")
    assert parse("0") == 0
    assert parse("1") == 1
    for c in "0123456789":
        assert parse(c) == float(c)

def test_multiple_digits():
    """ test multiple digits """
    print("test multiple digits...")
    assert parse("123") == 123
    assert parse("4567") == 4567

def test_decimal_points():
    """ test decimal points """
    print("test decimal points...")
    assert 123.4559999 <= parse("123.456") <= 123.4560001
    assert 0.45669999 <= parse(".4567") <= 0.45670001
    assert 4566.999 <= parse("4567.") <= 4567.00000001

def test_negative_numbers():
    """ test negative numbers """
    print("test negative numbers...")
    assert parse("-1") == -1
    assert parse("-4567") == -4567
    assert -4566.999 >= parse("-4567.") >= -4567.00000001



if __name__ == "__main__":
    test_single_digits()
    test_multiple_digits()
    test_decimal_points()
    test_negative_numbers()
    print("done.")
