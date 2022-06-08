import os

import pytest

import server.FileService


def test_delete_file(test_dir, create_files):
    for filename in create_files.keys():
        assert os.path.exists(filename)
        server.FileService.delete_file(filename)
        assert not os.path.exists(filename)


def test_file_not_exists(test_dir):
    with pytest.raises(RuntimeError):
        server.FileService.delete_file("non_existing_file")
