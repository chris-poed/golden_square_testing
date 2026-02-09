from lib.string_builder import *

def test_returns_string_when_passed_one_string():
    string_builder = StringBuilder()
    string_builder.add('hello')
    assert string_builder.output() == 'hello'

def test_returns_correct_string_length_when_passed_one_string():
    string_builder = StringBuilder()
    string_builder.add('hello')
    assert string_builder.size() == 5

def test_returns_correct_string_when_passed_two_strings():
    string_builder = StringBuilder()
    string_builder.add('hello ')
    string_builder.add('chris')
    assert string_builder.output() == 'hello chris'

def test_returns_correct_length_when_passed_two_strings():
    string_builder = StringBuilder()
    string_builder.add('hello ')
    string_builder.add('chris')
    assert string_builder.size() == 11
