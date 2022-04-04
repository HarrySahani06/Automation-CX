import pytest

#commands to execute specific testcase file to debugging
# pytest test_marker_ex.py -s -v -m "not functional"
# run this commad in terminal of pycharm once over the directory of testcases


@pytest.mark.functional
def test_login():
    print("Introducing first test case")
@pytest.mark.regresion
def test_login1():
    print("Introducing Second test case")
@pytest.mark.sanity
def test_login2():
    print("Introducing Third test case")
@pytest.mark.skip
def test_skip():
    print("skipping this testcase")


