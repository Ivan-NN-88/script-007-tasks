import os
from FileService import create_file, delete_file


def test_create_file(directory_handler):
    """Сhecks сorrect file creation."""
    # Before creating a file, I make sure that there is no such file.
    if os.path.exists(directory_handler):
        delete_file(directory_handler)
    assert not os.path.exists(directory_handler)

    # I make sure that the file has been created and returned a data dictionary with certain keys|values.
    result = create_file(directory_handler, b'Test text.')
    assert os.path.exists(directory_handler)
    assert isinstance(result, dict)
    assert 'name' in result
    assert result['name'] == os.path.split(directory_handler)[-1]
