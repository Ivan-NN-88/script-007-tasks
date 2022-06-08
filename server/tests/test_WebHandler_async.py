import os
from http import HTTPStatus

import pytest

import server.WebHandler
import utils.FileUtils
import utils.StrUtils


@pytest.mark.parametrize("filename, content, exists", [
    ('README1.txt', b'123', False),
    ('README1.txt', b'12', True),  # shorter size, same file
    ('README2.txt', b'1\\2/3:4{}5\n6\r7', False),  # use different symbols
])
async def test_create_file(filename, content, exists, aiohttp_client, unused_tcp_port_factory, test_dir):
    app = server.WebHandler.get_aiohttp_server()
    client = await aiohttp_client(app, server_kwargs={'port': unused_tcp_port_factory()})

    target = test_dir / filename
    assert target.exists() == exists

    resp = await client.post('/files', json={
        'filename': filename,
        'content': utils.StrUtils.bytes2str(content),
    })
    assert resp.status == HTTPStatus.OK
    resp_json = await resp.json()
    assert resp_json.get('status') == 'success'

    assert target.exists()
    assert target.read_bytes() == content
