import pytest


@pytest.fixture(scope='session')
def session():
    print("session start")
    yield
    print("\nsession end")


@pytest.fixture(scope='session', autouse=True)
def autouse():
    print("autouse start")
    yield
    print("\nautouse end")

@pytest.fixture(scope='module')
def module():
    print("Module start")
    yield
    print("\nModule End")

@pytest.fixture(scope='function')
def function():
    print("Function start")
    yield
    print("\nFunction end")
