from lib.greet import *
import pytest

@pytest.mark.it("Returns correct greeting with Chris")
def test_returns_correct_greeting_with_Chris():
    assert greet('Chris') == 'Hello, Chris!'

def test_returns_message_when_passed_empty_name():
    assert greet('') == 'Please enter a name'