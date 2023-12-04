from .day1 import validate, get_first_digit, get_last_digit

def test_validate_with_known():
    assert validate("1abc2") == 12
    assert validate("pqr3stu8vwx")  == 38
    assert validate("a1b2c3d4e5f") == 15
    assert validate("treb7uchet") == 77
    assert validate("two1nine") == 29
    assert validate("eightwothree") == 83
    assert validate("abcone2threexyz") == 13
    assert validate("xtwone3four") == 24
    assert validate("4nineeightseven2") == 42
    assert validate("zoneight234") == 14
    assert validate("7pqrstsixteen") == 76

def test_get_first_digit():
    assert get_first_digit("123") == 1
    assert get_first_digit("x3x") == 3
    assert get_first_digit("one23") ==  1

def test_get_last_digit():
    assert get_last_digit("123") == 3
    assert get_last_digit("12three") == 3
    assert get_last_digit("1threex") == 3
    assert get_last_digit("three") == 3

