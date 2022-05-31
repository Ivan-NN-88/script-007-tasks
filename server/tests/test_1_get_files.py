from FileService import get_files


def test_get_files():
    """Checking for information about all files in the working directory."""
    assert isinstance(get_files(), list)
