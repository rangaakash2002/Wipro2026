import pytest

def test_add():
    assert 2 + 2 == 4



#4
@pytest.fixture
def setup_teardown():
    print("setup")
    yield
    print("teardown")

def test_example(setup_teardown):
    print("test runner")

def test_example0(setup_teardown):
    print("test report")

def test_example1(setup_teardown):
    print("configuration files")



#5


def test_multi():
    assert 10*3==30