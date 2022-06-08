import json

import requests


def test_create_file(obj_info):
    """Checks the request to create a file."""
    domain = obj_info[0]
    tmp_file_name = obj_info[2]
    test_data = 'New file content\r\nСодержит две строки на разных языках!'
    headers = {'Content-type': 'text/html'}

    response = requests.post(f'{domain}/files/{tmp_file_name}',
                             data=test_data.encode('utf-8'),
                             headers=headers)
    assert response.status_code == 200
    pretty_response = json.loads(response.text)
    assert pretty_response['data']['content'] == test_data

    # Deleting a tmp file for the test.
    requests.delete(f'{domain}/files/{tmp_file_name}')
