import numb3rs

def test_valid_ip():
    assert numb3rs.validate("192.168.0.1") == True
    assert numb3rs.validate("255.255.255.0") == True
    assert numb3rs.validate("0.0.0.0") == True

def test_invalid_ip():
    assert numb3rs.validate("256.0.0.0") == False
    assert numb3rs.validate("192.168.0") == False
    assert numb3rs.validate("192.168.0.1.2") == False
    assert numb3rs.validate("192.168.0.-1") == False
    assert numb3rs.validate("192.168.0.foo") == False