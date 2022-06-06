import os
import pytest
import requests

from config.config import config

domain = 'http://127.0.0.1:8080'
file_dir = 'tmp'
file_name = 'tmp.txt'


@pytest.fixture(scope='session')
def directory_remover(request):
    def remover():
        """Remove tmp directory."""
        requests.post(f'{domain}/change_dir/back')
        requests.delete(f'{domain}/files/{file_dir}')

    remover()
    yield   # Run tests.
    remover()


@pytest.fixture()
def obj_info(directory_remover):
    # Preparation.
    requests.post(f'{domain}/change_dir/{file_dir}')

    # Run tests.
    yield domain, file_dir, file_name

    # Return to the main tmp directory.
    requests.post(f'{domain}/change_dir/back')
