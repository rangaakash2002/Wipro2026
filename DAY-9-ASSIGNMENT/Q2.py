#1

import pytest
def test_add():
    assert 2+3==5

def test_sub():
    assert 10-6==4

def test_multi():
    assert 10*3==30

def test_divide():
    assert 10/2==5


#2

import pytest
@pytest.fixture(scope="session")
def setup():
    print("setup browser")
    yield
    print("close browser")



#3

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b


