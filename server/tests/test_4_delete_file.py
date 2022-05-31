from FileService import delete_file, create_file


filename = 'tmp.txt'


def test_delete_file():
    create_file(filename)
    assert delete_file(filename) is None
