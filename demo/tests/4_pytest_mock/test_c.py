import pytest

import c


def test_a_const(mocker):
    # mocking the module when it is imported, not where A_CONSTANT is from
    mocker.patch.object(c, 'A_CONSTANT', 10)
    assert 20 == c.c_const()

    # you may mock twice or more times if you needed
    mocker.patch.object(c, 'A_CONSTANT', 11)
    assert 22 == c.c_const()


@pytest.mark.skip
def test_c_func_as_is():
    assert 6 == c.c_func()


def test_c_func(mocker):
    mocker.patch(
        'c.a_func',
        return_value=12
    )
    assert 36 == c.c_func()


def test_class_method(mocker):
    def my_replacement(self):
        return 4

    mocker.patch(
        'c.AClass.do_something',
        my_replacement
    )
    assert 16 == c.c_class()
