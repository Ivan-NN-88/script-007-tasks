from FileService import get_files


def test_get_files():
    assert isinstance(get_files(), list)
