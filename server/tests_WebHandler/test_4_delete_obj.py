import requests


def test_delete_obj(obj_info):
    """Checks the request to delete a directory/file."""
    domain = obj_info[0]
    tmp_dir_name = obj_info[1]
    tmp_file_name = obj_info[2]

    # Creating a directory and a file to check.
    requests.post(f'{domain}/change_dir/{tmp_dir_name}')
    requests.post(f'{domain}/files/{tmp_file_name}')

    # Deleting a file.
    response = requests.delete(f'{domain}/files/{tmp_file_name}')
    assert response.status_code == 200
    assert 'success' in response.text

    # Deleting a directory.
    requests.post(f'{domain}/change_dir/back')
    response = requests.delete(f'{domain}/files/{tmp_dir_name}')
    assert response.status_code == 200
    assert 'success' in response.text
