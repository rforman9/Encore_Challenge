import pytest
from rformanChallenge.arrayOps import flatten

NESTED_ARRAY = [[1, 2, [3]], 4]
SAMPLE_TEMPS = [78, 24, 32, 110, 58]


def test_flatten():
    """should return flattened array """
    flattened = flatten(NESTED_ARRAY)
    assert flattened == [1, 2, 3, 4]


def test_insert():
    from rformanChallenge.rfClasses import TempTracker
    tracked = TempTracker()
    for item in SAMPLE_TEMPS:
        tracked.insert(item)
    assert tracked.temps == SAMPLE_TEMPS


def test_max():
    from rformanChallenge.rfClasses import TempTracker
    tracked = TempTracker()
    for item in SAMPLE_TEMPS:
        tracked.insert(item)
    assert tracked.get_max() == 110


def test_min():
    from rformanChallenge.rfClasses import TempTracker
    tracked = TempTracker()
    for item in SAMPLE_TEMPS:
        tracked.insert(item)
    assert tracked.get_min() == 24


def test_mean():
    from rformanChallenge.rfClasses import TempTracker
    tracked = TempTracker()
    for item in SAMPLE_TEMPS:
        tracked.insert(item)
    assert tracked.get_mean() == 60
