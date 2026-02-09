from lib.report_length import *

def test_returns_correct_message_when_passed_hello():
    assert report_length('hello') == 'This string was 5 characters long.'

def test_returns_correct_when_passed_longer_string():
    assert report_length('dude wheres my car') == 'This string was 18 characters long.'