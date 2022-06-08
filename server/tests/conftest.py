import pathlib
import os

import pytest

import utils.Config
import utils.FileUtils


@pytest.fixture(scope='function')
def test_dir(tmp_path) -> pathlib.Path:
    with utils.FileUtils.remember_cwd():
        os.chdir(str(tmp_path))
        yield tmp_path
