from lib.check_codeword import *

def test_returns_correct_when_horse_is_used_as_codeword():
    assert check_codeword('horse') == 'Correct! Come in.'

def test_returns_close_message_when_passed_word_beginning_h_and_ending_e():
    assert check_codeword('house') == 'Close, but nope.'

def test_returns_wrong_when_passed_any_other_word():
    assert check_codeword('wrong password') == 'WRONG!'