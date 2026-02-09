import pytest
from lib.password_checker import *

def test_password_is_longer_than_or_equal_to_8_chars():
    password_checker = PasswordChecker()
    assert password_checker.check('abcd1234') == True

def test_password_is_less_than_8_chars():
    password_checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        password_checker.check('6chars')
    assert str(e.value) == 'Invalid password, must be 8+ characters.'

def test_password_throws_error_with_empty_string():
    password_checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        password_checker.check('')
    assert str(e.value) == 'Invalid password, must be 8+ characters.'