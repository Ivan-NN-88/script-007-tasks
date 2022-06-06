import os
from FileService import delete_obj, create_file, delete_obj


def test_delete_obj(directory_handler):
    """Сhecks сorrect file deletion."""
    # Before deleting, I make sure that there is such a file.
    create_file(directory_handler)
    assert os.path.exists(directory_handler)

    # I make sure that the file is deleted and no exceptions were raised.
    assert isinstance(delete_obj(directory_handler), str)
    assert not os.path.exists(directory_handler)
