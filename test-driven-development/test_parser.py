from parser import parse


def test_single_digits():
    assert parse("0") == 0
    assert parse("2") == 2
    assert parse("3") == 3
    assert parse("7") == 7
    assert parse("9") == 9


def test_multiple_digits():
    assert parse("22") == 22
    assert parse("321") == 321
    assert parse("333") == 333
    assert parse("345") == 345
    assert parse("3334567890") == 3334567890


def test_decimal_numbers():
    assert parse("22.234") == 22.234
    assert parse("32.1") == 32.1
    assert parse("333.2") == 333.2
    assert parse("345.6") == 345.6
    assert parse("333456.78902") == 333456.78902


def test_negative_numbers():
    assert parse("-7") == -7
    assert parse("-90") == -90
    assert parse("-90.7") == -90.7


def test_only_legal_characters_allowed():
    try:
        parse("1 23")
    except Exception as e:
        assert "error" in str(e).lower()
        return
    raise Exception("should have seen an error")


def test_rejects_multiple_decimal_points():
    try:
        parse("1.2.3")
    except Exception as e:
        assert "error" in str(e).lower()
        return
    raise Exception("should have seen an error")


def test_rejects_double_negative_sign():
    try:
        parse("--9")
    except Exception as e:
        assert "error" in str(e).lower()
        return
    raise Exception("should have seen an error")


def test_empty_string():
    try:
        parse("")
    except Exception as e:
        assert "error" in str(e).lower()
        return
    raise Exception("should have seen an error")
