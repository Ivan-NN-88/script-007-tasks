import requests


def test_change_dir(obj_info):
    """
    Checking the request for the correct modification of the working directory.
    """
    domain = obj_info[0]
    tmp_dir_name = obj_info[1]

    response = requests.post(f'{domain}/change_dir/{tmp_dir_name}')
    assert response.status_code == 200
    assert 'success' in response.text
