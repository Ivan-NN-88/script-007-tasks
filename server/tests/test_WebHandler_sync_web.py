import multiprocessing
import os
from http import HTTPStatus

import pytest
import requests
from aiohttp import web

import server.WebHandler
import utils.FileUtils
import utils.StrUtils
import utils.Config


def _run_webserver_helper(app, host, port):
    web.run_app(app, host=host, port=port)


@pytest.fixture(scope='function')
def web_server_up(unused_tcp_port_factory, test_dir):
    utils.Config.data.port = unused_tcp_port_factory()
    utils.Config.data.dir = str(test_dir)
    app = server.WebHandler.get_aiohttp_server()
    process = multiprocessing.Process(target=_run_webserver_helper, args=(
        app, utils.Config.data.host, utils.Config.data.port))
    process.start()
    yield f'http://{utils.Config.data.host}:{utils.Config.data.port}'
    process.terminate()
    process.join(5)


@pytest.mark.parametrize("filename, content, exists", [
    ('README1.txt', b'123', False),
    ('README1.txt', b'12', True),  # shorter size, same file
    ('README2.txt', b'1\\2/3:4{}5\n6\r7', False),  # use different symbols
])
def test_create_file(filename, content, exists, web_server_up, test_dir):
    target = test_dir / filename
    if exists:
        target.write_bytes(b'another string')

    resp = requests.post(
        url=f'{web_server_up}/files',
        json={
            'filename': filename,
            'content': utils.StrUtils.bytes2str(content),
        },
    )
    assert resp.status_code == HTTPStatus.OK
    resp_json = resp.json()
    assert resp_json.get('status') == 'success'

    assert target.exists()
    assert target.read_bytes() == content
