"""Working in the file server."""

# Python standard libraries.
import os
import time


def change_dir(path: str, autocreate: bool = True) -> None:
    """Change current directory of app.

    Args:
        path (str): Path to working directory with files.
        autocreate (bool): Create folder if it doesn't exist.

    Raises:
        RuntimeError: if directory does not exist and autocreate is False.
        ValueError: if path is invalid.
    """
    if autocreate and not os.path.exists(path):
        os.makedirs(path)
    os.chdir(path)


def get_files() -> list:
    """Get info about all files in working directory.

    Returns:
        List of dicts, which contains info about each file. Keys:
        - name (str): filename
        - create_date (datetime): date of file creation.
        - edit_date (datetime): date of last file modification.
        - size (int): size of file in bytes.
    """
    result = []

    for file in os.listdir(os.getcwd()):
        if not os.path.isfile(file):
            continue

        file_info = {
            'name': file,
            'create_date': time.ctime(os.path.getctime(file)),
            'edit_date': time.ctime(os.path.getmtime(file)),
            'size': os.path.getsize(file)
        }

        result.append(file_info)

    return result


def get_file_data(filename: str) -> dict:
    """Get full info about file.

    Args:
        filename (str): Filename.

    Returns:
        Dict, which contains full info about file. Keys:
        - name (str): filename
        - content (str): file content
        - create_date (datetime): date of file creation
        - edit_date (datetime): date of last file modification
        - size (int): size of file in bytes

    Raises:
        RuntimeError: if file does not exist.
        ValueError: if filename is invalid.
    """
    with open(filename, 'r') as file:
        data = file.read()

    file_info = {
        'name': os.path.split(filename)[1],
        'content': data,
        'create_date': time.ctime(os.path.getctime(filename)),
        'edit_date': time.ctime(os.path.getmtime(filename)),
        'size': os.path.getsize(filename)
    }

    return file_info


def create_file(filename: str, content: str = '') -> dict:
    """Create a new file.

    Args:
        filename (str): Filename.
        content (str): String with file content.

    Returns:
        Dict, which contains name of created file. Keys:
        - name (str): filename
        - content (str): file content
        - create_date (datetime): date of file creation
        - size (int): size of file in bytes

    Raises:
        ValueError: if filename is invalid.
    """
    path = os.path.normpath(filename)
    with open(path, 'w') as file:
        file.write(content)
    return get_file_data(path)


def delete_file(filename: str) -> None:
    """Delete file.

    Args:
        filename (str): filename

    Raises:
        RuntimeError: if file does not exist.
        ValueError: if filename is invalid.
    """
    os.remove(filename)
