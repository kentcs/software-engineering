def parse(s):
    """Parse a signed integer or decimal string into a numeric value."""
    assert s != "", "error in numeric string"

    sign = 1
    if s[0] == "-":
        s = s[1:]
        sign = -1

    assert s != "", "error in numeric string"

    n = 0
    decimal = False
    fraction = 0.1

    for c in s:
        assert c in "0123456789.", f"error: Illegal character: {c}"
        if c == ".":
            assert not decimal, f"error: Illegal decimal point in: {s}"
            decimal = True
            continue
        if decimal:
            n = n + (ord(c) - ord("0")) * fraction
            fraction = fraction / 10
        else:
            n = n * 10 + ord(c) - ord("0")

    return n * sign
