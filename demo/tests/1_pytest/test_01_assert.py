import pytest
import sys

from demo.tests.myfuncs import myadd


def test_myadd():
    assert 10 == myadd(7, 3)

# Not best implementation - see next files
def test_myadd_dataset():
    myadd_dataset = [
        0, 0, 0,
        1, 2, 3,
        11, -5, 6,
        # 11, 5,  6,  # broken
    ]

    for i in range(0, len(myadd_dataset), 3):
        a, b, c = myadd_dataset[i:i + 3]
        # assert is not a function!
        assert c == myadd(a, b)


# skip always
@pytest.mark.skip(reason="no way of currently testing this")
def test_myadd_bigint():
    assert 10 == myadd(7, 3)

# skip during execution
def test_depend_os():
    if sys.platform == 'win32':
        pytest.skip("unsupported OS")
    assert 10 == myadd(7, 3)

# skip before running test
@pytest.mark.skipif(sys.version_info < (3, 7), reason="requires python3.7 or higher")
def test_depend_python_version():
    assert True

@pytest.mark.xfail
def test_mark_failed():
    assert False
