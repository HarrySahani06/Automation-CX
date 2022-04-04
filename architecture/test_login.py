import pytest

def setup_module():
    print("establishing DB connection")

def teardown_module():
    print("clossing DB Connection")

def setup_function():
    print("Browser initiated")
def teardown_function():
    print("quitting browser")


def test_dologin():
    print("Testcase Exeuted")

def test_dologin1():
    print("Testcase Exeuted1")