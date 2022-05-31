from FileService import create_file


filename = 'tmp.txt'


def test_create_file():
    assert isinstance(create_file(filename), dict)
