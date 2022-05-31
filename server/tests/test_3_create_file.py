from fileinput import filename
from FileService import create_file


def test_create_file(directory_handler):
    """Сhecks сorrect file creation."""
    assert isinstance(create_file(directory_handler), dict)
