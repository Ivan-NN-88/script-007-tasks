import os
from FileService import change_dir, create_file, get_file_data


def test_get_file_data(directory_handler):
    """Checks whether the file data is received correctly."""
    create_file(directory_handler)
    result = get_file_data(directory_handler)

    assert isinstance(result, dict)
    assert 'name' in result
    assert result['name'] == os.path.split(directory_handler)[1]
