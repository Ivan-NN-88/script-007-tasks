import os
from http import HTTPStatus

import pytest
import requests

import utils.Config
import utils.FileUtils
import utils.NetUtils
import utils.StrUtils

# These tests assume that you have running web-server.
#
# Such approach has the following disadvantages:
# - you may not change settings of running application
#   can't work in temporary folder -> tests may change production data
# - you can be sure that current state is suitable with tests
#   some preconditions may not met
# - you can't run tests in parallel

BASE_API_URL = f'http://{utils.Config.data.host}:{utils.Config.data.port}'

is_port_open = utils.NetUtils.is_tcp_port_open(
    host=utils.Config.data.host,
    port=utils.Config.data.port
)

@pytest.fixture(scope='module')
def prepare_data_dir():
    data_dir = utils.Config.get_project_dir(utils.Config.data.dir)
    filenames = ['README1.txt', 'README2.txt']

    def clean_up():
        for filename in filenames:
            target = os.path.join(data_dir, filename)
            utils.FileUtils.delete_files(target)

    clean_up()
    yield data_dir
    clean_up()


@pytest.mark.skipif(not is_port_open, reason='server is not running')
@pytest.mark.parametrize("filename, content, exists", [
    ('README1.txt', b'123', False),
    ('README1.txt', b'12', True),  # shorter size, same file
    ('README2.txt', b'1\\2/3:4{}5\n6\r7', False),  # use different symbols
])
def test_create_file(filename, content, exists, prepare_data_dir):
    target = os.path.join(prepare_data_dir, filename)
    assert os.path.exists(target) == exists

    resp = requests.post(
        url=f'{BASE_API_URL}/files',
        json={
            'filename': filename,
            'content': utils.StrUtils.bytes2str(content),
        },
    )
    assert resp.status_code == HTTPStatus.OK
    resp_json = resp.json()
    assert resp_json.get('status') == 'success'

    assert os.path.exists(target)
    with open(target, mode='rb') as f:
        new_content = f.read()
        assert content == new_content
