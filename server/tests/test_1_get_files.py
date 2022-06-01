import os
from FileService import change_dir, create_file, get_files


def test_get_files(directory_handler):
    """Checking for information about all files in the working directory."""
    create_file(directory_handler)
    result = get_files()

    assert isinstance(get_files(), list)
    assert result[0]['name'] == os.path.split(directory_handler)[1]
