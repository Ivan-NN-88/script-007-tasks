import contextlib
import glob
import os
import shutil
import stat


@contextlib.contextmanager
def remember_cwd():
    curdir = os.getcwd()
    try:
        yield
    finally:
        os.chdir(curdir)


def rm(path):
    if not os.path.exists(path):
        return

    if os.path.isdir(path):
        shutil.rmtree(path)
    else:
        os.remove(path)


def delete_files(*patterns) -> None:
    """Iterate over the list of filepaths & remove each file.

    Args:
        patterns: (str) shell patterns for files (or just filenames)
    """

    def _on_rm_error(func, path, exc_info):
        # path contains the path of the file that couldn't be removed
        # let's just assume that it's read-only and unlink it.
        os.chmod(path, stat.S_IWRITE)
        os.unlink(path)

    for pattern in patterns:
        filelist = glob.glob(pattern, recursive=True)
        for filepath in filelist:
            if os.path.isdir(filepath):
                shutil.rmtree(filepath, onerror=_on_rm_error)
            else:
                os.remove(filepath)
