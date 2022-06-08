import os
import subprocess
import sys


def capture(args=[], timeout=None):
    proc = subprocess.Popen(
        [sys.executable, *args],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env={**os.environ, 'PYTHONIOENCODING': 'utf-8'},
    )
    out, err = proc.communicate(timeout=timeout)
    return out, err, proc.returncode

# As for now, there is no built-in way to detect running from pytest
# https://docs.pytest.org/en/latest/example/simple.html#detect-if-running-from-within-a-pytest-run
# https://github.com/pytest-dev/pytest/issues/9502
# https://stackoverflow.com/questions/25188119/test-if-code-is-executed-from-within-a-py-test-session
def is_pytest_running():
    return 'pytest' in sys.modules or \
        os.path.basename(sys.argv[0]) in (
            'pytest',
            'py.test',
            'testlauncher.py', # VS Code
        )
