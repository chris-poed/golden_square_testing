import pytest
from lib.present import *

def test_present_is_successfully_unwrapped_when_passed_present():
    present = Present()
    present.wrap('tv')
    assert present.unwrap() == 'tv'

def test_error_thrown_when_contents_already_wrapped():
    present = Present()
    present.wrap('tv')
    with pytest.raises(Exception) as e:
        present.wrap('bike')
    assert str(e.value) == 'A contents has already been wrapped.'

def test_error_thrown_when_no_contents_have_been_wrapped():
    present = Present() 
    with pytest.raises(Exception) as e:
        present.unwrap()
    assert str(e.value) == 'No contents have been wrapped.'

def test_wrapping_doesnt_overwrite_existing_wrapped_present():
    present = Present()
    present.wrap('tv')
    with pytest.raises(Exception) as e:
        present.wrap('bike')
    assert present.unwrap() == 'tv'