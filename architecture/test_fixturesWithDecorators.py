import pytest


@pytest.fixture(scope='module')
def setup():
    print("establishing DB Connections")

    #yeilds act as teardown method
    yield
    print("closing DB connections")

@pytest.fixture(scope='function')
def before():
    print("before Testcase")

    yield
    print("after testcase")



# def test_dologin():
#     print("Testcase Exeuted")
#
# def test_dologin1(setup,before):
#     print("Testcase Exeuted1")


@pytest.mark.usefixtures("setup","before")
def test_dologin():
    print("Testcase Exeuted")
@pytest.mark.usefixtures("setup","before")
def test_dologin1(setup,before):
    print("Testcase Exeuted1")