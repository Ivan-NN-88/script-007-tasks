import os

import server.FileService


def test_get_files(test_dir, create_files):
    files = server.FileService.get_files()
    assert isinstance(files, list) and len(files) == len(create_files)

    filenames = sorted([file['name'] for file in files])
    assert list(create_files.keys()) == filenames

    for file in files:
        assert isinstance(file, dict) and len(file.keys()) == 3
        props = create_files[file['name']]
        assert file['edit_date'] == props['mtime']
        assert file['size'] == props['size']
