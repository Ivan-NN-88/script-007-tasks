import json

import requests


def test_get_files(obj_info):
    """
    Checking the request for information about all files in
    the working directory.
    """
    domain = obj_info[0]
    tmp_file_name = obj_info[2]

    # Creating a tmp file for the test.
    requests.post(f'{domain}/files/{tmp_file_name}', data='TEST')

    response = requests.get(f'{domain}/files')
    assert response.status_code == 200
    pretty_response = json.loads(response.text)
    assert pretty_response['data'][0]['name'] == tmp_file_name

    # Deleting a tmp file for the test.
    requests.delete(f'{domain}/files/{tmp_file_name}')
