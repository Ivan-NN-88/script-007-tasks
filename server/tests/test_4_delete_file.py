import os
from FileService import delete_file, create_file


def test_delete_file(directory_handler):
    """Сhecks сorrect file deletion."""
    create_file(directory_handler)
    assert delete_file(directory_handler) is None and not os.path.exists(directory_handler)
