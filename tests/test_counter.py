from lib.counter import *

def test_counter_reports_the_correct_count_so_far():
    counter = Counter()
    counter.add(3)
    assert counter.report() == 'Counted to 3 so far.'

def test_counter_reports_correct_count_when_given_multiple_adds():
    counter = Counter()
    counter.add(3)
    counter.add(7)
    assert counter.report() == 'Counted to 10 so far.'