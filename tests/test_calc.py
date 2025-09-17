import pytest
from src.calc import add, sub

# pass/fail/error/skip/xfail/xpass test cases
# pytest -v
# ============================= test session starts ==============================
# tests/test_calc.py::test_add PASSED                                                                                                                      [ 14%] 
# tests/test_calc.py::test_sub PASSED                                                                                                                      [ 28%] 
# tests/test_calc.py::test_fail FAILED                                                                                                                     [ 42%]
# tests/test_calc.py::test_skip SKIPPED (not yet ready to run)                                                                                             [ 57%] 
# tests/test_calc.py::test_expected_fail XFAIL (need to fix bug #123)                                                                                      [ 71%]
# tests/test_calc.py::test_error FAILED                                                                                                                    [ 85%]
# tests/test_calc.py::test_xpass XPASS (this test is expected to fail but will pass. so need to be fixed)    


def test_add():
    assert add(2, 4) == 6

def test_sub():
    assert sub(4, 2) == 2

def test_fail():
    assert sub(4, 2) == 1

@pytest.mark.skip(reason="not yet ready to run")
def test_skip():
    assert add(1, 1) == 3

@pytest.mark.xfail(reason="need to fix bug #123")
def test_expected_fail():
    assert add(2, 2) == 5

# @pytest.mark.error
def test_error():
    from src import calc
    calc.multiply(2, 3)  
    # raise Exception("This test raises an exception")

@pytest.mark.xfail(reason="this test is expected to fail but will pass. so need to be fixed")
def test_xpass():
    assert add(3, 3) == 6  # This test is expected to fail but will pass
