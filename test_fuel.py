import fuel


def test_convert_valid_input():
    assert fuel.convert("1/2") == 50
    assert fuel.convert("3/4") == 75
    assert fuel.convert("0/1") == 0
    assert fuel.convert("1/1") == 100


def test_convert_invalid_input():
    try:
        fuel.convert("2/1")
    except ValueError as e:
        assert str(e) == "X cannot be greater than Y."
    else:
        assert False

    try:
        fuel.convert("1/0")
    except ZeroDivisionError as e:
        assert str(e) == "Denominator cannot be zero."
    else:
        assert False


def test_gauge():
    assert fuel.gauge(0) == "E"
    assert fuel.gauge(1) == "E"
    assert fuel.gauge(50) == "50%"
    assert fuel.gauge(99) == "F"
    assert fuel.gauge(100) == "F"
