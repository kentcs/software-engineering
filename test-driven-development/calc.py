def parse(s): # return the numeric value of the string s
    assert s!="","error in numeric string"
    sign = 1
    if s[0] == "-":
        s = s[1:]
        sign = -1
    n = 0
    decimal = False
    fraction = 0.1
    for c in s:
        assert c in "0123456789.", f"error: Illegal character: {c}"
        if c == ".":
            assert not decimal, f"error: Illegal decimal point in : {s}"
            decimal = True
            continue
        if decimal:
            n = n + (ord(c) - ord("0")) * fraction
            fraction = fraction / 10
        else:
            n = n * 10
            n = n +  ord(c) - ord("0")
    return n * sign

# it should return 0 for "0"
def test_single_digit():
    print("testing single digit...")
    assert parse("0") == 0
    assert parse("7") == 7
    assert parse("9") == 9

# for multiple digits, it should return the integer
def test_multiple_digits():
    print("testing multiple digits...")
    v = parse("321")
    assert v == 321, f"Expected {321}, got {v}"
    v = parse("333")
    assert v == 333, f"Expected {333}, got {v}"
    v = parse("3334567890")
    assert v == 3334567890, f"Expected {3334567890}, got {v}"

def test_only_legal_characters_allowed():
    print("testing only legal characters allowed...")
    try:
        parse("1 23")
    except Exception as e:
        assert "error" in str(e).lower() 
        return
    raise Exception("should have seen an error")

def test_decimal_numbers():
    print("testing decimal numbers...")
    v = parse("32.1")
    assert v == 32.1, f"Expected {32.1}, got {v}"
    v = parse("333.2")
    assert v == 333.2, f"Expected {333.2}, got {v}"
    v = parse("333456.78902")
    assert v == 333456.78902, f"Expected {333456.78902}, got {v}"
    try:
        parse("1.2.3")
    except Exception as e:
        assert "error" in str(e).lower() 
        return
    raise Exception("should have seen an error with {'1.2.3'}")

def test_negative_numbers():
    print("testing negative numbers...")
    assert parse("-7") == -7
    assert parse("-90") == -90
    assert parse("-90.7") == -90.7
    try:
        parse("--9")
    except Exception as e:
        assert "error" in str(e).lower() 
        return
    raise Exception("should have seen an error with {'1.2.3'}")


# it should return an error for "" containing "error"
def test_empty_string():
    print("testing empty string...")
    try:
        parse("")
    except Exception as e:
        assert "error" in str(e).lower() 
        return
    raise Exception("should have seen an error")

if __name__ == "__main__":
    print("testing...")
    test_empty_string()
    test_single_digit()
    test_multiple_digits()
    test_only_legal_characters_allowed()
    test_decimal_numbers()
    test_negative_numbers()
    print("done.")