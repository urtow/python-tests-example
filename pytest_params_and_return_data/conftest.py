import pytest


@pytest.fixture
def return_true():
    return True


@pytest.fixture
def return_false():
    return False


@pytest.fixture
def yield_true():
    yield True


@pytest.fixture
def yield_false():
    yield False

@pytest.fixture
def deep(deeper):
    print("Deep")


@pytest.fixture
def deeper():
    print("Deeper")

@pytest.fixture(params=[True, False, 1, 0])
def fixture_with_param(request):
    return request.param
