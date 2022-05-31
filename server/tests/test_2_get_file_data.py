from FileService import create_file, get_file_data


def test_get_file_data(directory_handler):
    """Checks whether the file data is received correctly."""
    create_file(directory_handler)
    assert isinstance(get_file_data(directory_handler), dict)
