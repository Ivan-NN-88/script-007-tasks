import os
import pytest
from time import sleep


file_name = 'tmp.txt'
file_dir = fr'{os.getcwd()}\tmp'
file_path = fr'{file_dir}\{file_name}'


@pytest.fixture(scope='session')
def directory_remover(request):
    # Run tests.
    yield

    # Remove tmp directory.
    if os.path.exists(file_dir):
        os.chdir(os.path.split(file_dir)[0])
        os.rmdir(file_dir)


@pytest.fixture()
def directory_handler(directory_remover):
    # Run tests.
    yield file_path

    # Remove tmp file.
    if os.path.exists(file_path):
        os.remove(file_path)
