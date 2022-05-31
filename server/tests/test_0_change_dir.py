import os
from FileService import change_dir


def test_change_dir(directory_handler):
    """Checking the correct change of the working directory."""
    assert change_dir(fr'{os.getcwd()}\tmp') is None
