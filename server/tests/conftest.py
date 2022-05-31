import os
import pytest
from time import sleep


file_name = 'tmp.txt'
file_dir = fr'{os.getcwd()}\tmp'
file_path = fr'{file_dir}\{file_name}'


@pytest.fixture()
def directory_handler(request):
    # Run tests.
    yield file_path

    # Remove tmp file.
    if os.path.exists(file_path):
        os.remove(file_path)
