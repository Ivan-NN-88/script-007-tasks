import contextlib
import os

import pytest


# tmp_path is build-in fixture in pytest
# https://docs.pytest.org/en/latest/how-to/tmp_path.html#the-tmp-path-fixture
def test_create_file(tmp_path):
    print(f"1>{tmp_path}<")  # str(tmp_path), use -s to see output

    d = tmp_path / "sub"
    d.mkdir()
    p = d / "hello.txt"
    content = 'abcd'
    p.write_text(content)
    assert p.read_text() == content
    assert len(list(tmp_path.iterdir())) == 1


@contextlib.contextmanager
def remember_cwd():
    curdir = os.getcwd()
    try:
        yield
    finally:
        os.chdir(curdir)


@pytest.fixture(scope='function')
def change_test_dir(tmp_path):
    with remember_cwd():
        os.chdir(str(tmp_path))
        yield str(tmp_path)


def test_nothing(change_test_dir):
    print(f"2>{change_test_dir}<")  # another value of tmp_path
    print(f"3>{os.getcwd()}")
