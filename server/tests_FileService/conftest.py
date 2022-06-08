import datetime
import os
import pathlib
from typing import Dict, Tuple

import pytest

import utils.FileUtils
import utils.TimeUtils


@pytest.fixture(scope='function')
def test_dir(tmp_path) -> pathlib.Path:
    with utils.FileUtils.remember_cwd():
        os.chdir(str(tmp_path))
        yield tmp_path


@pytest.fixture(scope='function')
def create_files() -> Dict[str, Dict]:

    def get_past_days_datetime(days: int) -> datetime.datetime:
        """Get datetime for n days ago without microseconds"""
        n = datetime.datetime.now().replace(microsecond=0)
        return n - datetime.timedelta(days=days)

    files = {
        # no ctime:
        # https://stackoverflow.com/questions/5803765/is-there-anyway-to-modify-stat-information-like-mtime-or-ctime-manually-in-pytho
        'README1.txt': {
            'content': b'123',
            'atime': get_past_days_datetime(0),
            'mtime': get_past_days_datetime(1),
            'size': 3,
        },
        'README2.txt': {
            'content': b'1\\2/3:4{}5\n6\r7',
            'atime': get_past_days_datetime(3),
            'mtime': get_past_days_datetime(2),
            'size': 14,
        },
    }
    for filename, props in files.items():
        p = pathlib.Path(filename)
        p.write_bytes(props['content'])
        atime = utils.TimeUtils.datatime_to_floattime(props['atime'])
        mtime = utils.TimeUtils.datatime_to_floattime(props['mtime'])
        os.utime(p, (atime, mtime))
    yield files
