import os
from FileService import delete_file, create_file


def test_delete_file(directory_handler):
    """Сhecks сorrect file deletion."""
    # Before deleting, I make sure that there is such a file.
    create_file(directory_handler)
    assert os.path.exists(directory_handler)

    # I make sure that the file is deleted and no exceptions were raised.
    assert delete_file(directory_handler) is None
    assert not os.path.exists(directory_handler)
