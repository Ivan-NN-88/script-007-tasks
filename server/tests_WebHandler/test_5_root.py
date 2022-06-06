import requests


def test_root(obj_info):
    """Checks the main page of the file server"""
    domain = obj_info[0]

    response = requests.get(domain)
    assert response.status_code == 200
    assert 'success' in response.text
