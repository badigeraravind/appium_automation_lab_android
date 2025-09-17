from utils.math_utils import add, is_even

def test_add():
    assert add(2,3) == 5
    assert add(4,5) != 8

def test_is_even():
    assert is_even(4) is True
    assert is_even(9) is False