import pytest


def test_1(return_true):
    assert return_true


def test_2(return_false):
    assert return_false


def test_3(yield_true):
    assert yield_true


def test_4(yield_false):
    assert yield_false


def test_deep(deep):
    assert True


@pytest.mark.parametrize("first,second",[
    (1,2),
    (1,1)
    ])
def test_with_param(first, second):
    assert first == second


def test_with_paramed_fixture(fixture_with_param):
    assert fixture_with_param
