import json

import requests


def test_get_file_data(obj_info):
    """Checks the request to get the file data."""
    domain = obj_info[0]
    tmp_file_name = obj_info[2]

    # Creating a file to check.
    requests.post(f'{domain}/files/{tmp_file_name}')

    response = requests.get(f'{domain}/files/{tmp_file_name}')
    assert response.status_code == 200
    pretty_response = json.loads(response.text)
    assert pretty_response['data']['name'] == tmp_file_name

    # Deleting a file to check.
    requests.delete(f'{domain}/files/{tmp_file_name}')
