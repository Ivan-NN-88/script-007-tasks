import os
import sys

import pytest

import server.FileService


@pytest.mark.parametrize('filename, content',
                         [('tmp1', b'111'), ('tmp2', b'222'), ('tmp3', b'333')])
def test_create_file_fullname(filename, content, test_dir):
    full_path = str(test_dir / filename)
    assert not os.path.exists(full_path)
    result = server.FileService.create_file(full_path, content)
    assert isinstance(result, dict)
    assert os.path.exists(full_path)
    assert (test_dir / filename).read_bytes() == content


@pytest.mark.skipif(sys.platform != 'win32', reason='windows only')
@pytest.mark.parametrize('filename', [('tmp"1'), ("tm>p2"), ('tmp*3')])
def test_bad_filename(filename, test_dir):
    with pytest.raises(ValueError):
        server.FileService.create_file(filename, b'')
