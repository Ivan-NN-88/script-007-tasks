import pytest

import b


def test_a_const(mocker):
    mocker.patch.object(b.a, 'A_CONSTANT', 10)
    assert 20 == b.b_const()

    # you may mock twice or more times if you needed
    mocker.patch.object(b.a, 'A_CONSTANT', 11)
    assert 22 == b.b_const()


@pytest.mark.skip
def test_b_funb_as_is():
    assert 6 == b.b_func()


def test_b_func(mocker):
    mocker.patch(
        'b.a.a_func',
        return_value=12
    )
    assert 36 == b.b_func()


def test_class_method(mocker):
    def my_replacement(self):
        return 4

    mocker.patch(
        'b.a.AClass.do_something',
        my_replacement
    )
    assert 16 == b.b_class()
