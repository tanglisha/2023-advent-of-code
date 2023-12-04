from .day1 import validate

def test_validate_with_known():
    assert validate("1abc2") == 12
    assert validate("pqr3stu8vwx")  == 38
    assert validate("a1b2c3d4e5f") == 15
    assert validate("treb7uchet") == 77

