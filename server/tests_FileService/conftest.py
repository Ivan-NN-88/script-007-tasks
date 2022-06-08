import os
import pytest
from shutil import rmtree

from FileService import change_dir
from config.config import config

file_name = 'tmp.txt'
file_dir = os.path.join(config.main_dir, 'tmp')
file_path = os.path.join(file_dir, file_name)


@pytest.fixture(scope='session')
def directory_remover(request):

    def remover():
        """Remove tmp directory."""
        if os.path.exists(file_dir):
            os.chdir(os.path.split(file_dir)[0])
            rmtree(file_dir)

    remover()
    yield  # Run tests.
    remover()


@pytest.fixture()
def directory_handler(directory_remover):
    # Preparation.
    change_dir(file_dir)

    # Run tests.
    yield file_path

    # Remove tmp file.
    if os.path.exists(file_path):
        os.remove(file_path)
