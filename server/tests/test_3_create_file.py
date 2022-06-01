import os
from FileService import create_file, delete_file


def test_create_file(directory_handler):
    """Сhecks сorrect file creation."""
    try:
        delete_file(directory_handler)
    except FileNotFoundError:
        ...
    assert not os.path.exists(directory_handler)

    result = create_file(directory_handler)
    assert os.path.exists(directory_handler)
    assert isinstance(result, dict)
    assert 'name' in result
    assert result['name'] == os.path.split(directory_handler)[1]
