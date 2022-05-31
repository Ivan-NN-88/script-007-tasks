from FileService import create_file, get_file_data


filename = 'tmp.txt'


def test_get_file_data():
    create_file(filename)
    assert isinstance(get_file_data(filename), dict)
