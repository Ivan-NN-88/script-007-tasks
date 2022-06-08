import os

from FileService import create_file, get_file_data


def test_get_file_data(directory_handler):
    """Checks whether the file data is received correctly."""
    create_file(directory_handler)
    result = get_file_data(directory_handler)

    # The result should be a dictionary with specific keys and values.
    assert isinstance(result, dict)
    assert 'name' in result
    assert result['name'] == os.path.split(directory_handler)[-1]
