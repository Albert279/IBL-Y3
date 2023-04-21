import bank
def test_value_hello():
    assert bank.value("hello world") == 0
    assert bank.value("HELLO") == 0
    assert bank.value("hello123") == 0
def test_value_h():
    assert bank.value("hi") == 20
    assert bank.value("Hi") == 20
    
