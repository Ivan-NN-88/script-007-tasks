import pytest


# https://docs.pytest.org/en/latest/how-to/tmp_path.html#the-tmp-path-factory-fixture
@pytest.fixture(scope="session")
def prepare_testfiles(tmp_path_factory):
    datadir = tmp_path_factory.mktemp('data')

    filename = datadir / 'hello.txt'
    filename.write_text('abcd')

    return datadir
