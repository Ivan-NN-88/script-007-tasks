import os

from FileService import change_dir


def test_change_dir(directory_handler):
    """Checking the correct change of the working directory."""
    main_path = os.path.split(directory_handler)[0]
    tmp_path = os.path.split(main_path)[0]

    # Directories should not be equal.
    os.chdir(tmp_path)
    assert os.getcwd() != main_path

    # Directories must be equal.
    change_dir(main_path)
    assert os.getcwd() == main_path
