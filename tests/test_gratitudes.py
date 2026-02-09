from lib.gratitudes import *

def test_returns_correct_message_when_passed_gratitude():
    gratitudes = Gratitudes()
    gratitudes.add('coding')
    assert gratitudes.format() == 'Be grateful for: coding'
