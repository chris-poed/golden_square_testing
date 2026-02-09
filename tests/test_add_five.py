from lib.add_five import *

def test_add_five_returns_eight_for_three():
    expected = 8
    actual = add_five(3)
    
    assert expected == actual
