import os
from FileService import change_dir


def test_change_dir():
    assert change_dir(fr'{os.getcwd()}\tmp') is None
