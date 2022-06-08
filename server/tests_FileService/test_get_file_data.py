import os

import server.FileService


def test_get_file_data(test_dir, create_files):
    for filename, props in create_files.items():
        assert os.path.exists(filename)
        res = server.FileService.get_file_data(filename)
        assert isinstance(res, dict) and len(res.keys()) == 4
        assert res['name'] == filename
        assert res['content'] == props['content']
        assert res['edit_date'] == props['mtime']
        assert res['size'] == props['size']
