# see conftest.py for prepare_testfiles
def test_histogram(prepare_testfiles):
    p = prepare_testfiles / 'hello.txt'
    assert p.read_text() == 'abcd'
