import pytest


from exercises.ex2 import compute_average, STUDENT_DICT


def test_ex2_ok():
    """test ex2"""

    # case ok
    assert compute_average("Alice", STUDENT_DICT) == 0


def test_ex2_ko():
    """test ex2"""

    # case error
    assert compute_average("Julian", STUDENT_DICT) == 1
