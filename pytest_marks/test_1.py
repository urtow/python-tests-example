import pytest

p0 = pytest.mark.p0
p1 = pytest.mark.p1
p2 = pytest.mark.p2


@p0
def test_0():
    assert True

@p1
def test_1():
    assert True


@p2
def test_2():
    assert True
