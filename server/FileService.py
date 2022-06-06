"""Working in the file server."""

import logging
import os
import re
from shutil import rmtree
import time

from config.config import config


def __checking_path(path: str) -> bool:
    """Checks the path for the content of "..".

    Args:
        path (str): specify the path to check.

    Raises:
        ValueError: if path is invalid.
    """
    logging.info(f'Checking the path [{path}] for validity...')

    abs_path = os.path.abspath(path)

    if re.findall(r'[/\\].[/\\]|C[:/\\]+Windows', abs_path):
        raise ValueError(f'Path [{path}] is invalid!')
    if not config.main_dir in abs_path:
        raise ValueError(f'[{path}] - Are you trying to work outside the scope of the current project!')

    logging.info(f'Checking the path [{path}] for validity is completed.')


def change_dir(path: str, autocreate: bool = True) -> None:
    """Change current directory of app.

    Args:
        path (str): Path to working directory with files.
        autocreate (bool): Create folder if it doesn't exist.

    Raises:
        RuntimeError: if directory does not exist and autocreate is False.
        ValueError: if path is invalid.
    """
    logging.info(f'Changing the current application directory to [{path}]...')

    # Checking/creating a directory.
    __checking_path(path)
    path_exists = os.path.exists(path)
    if autocreate and not path_exists:
        logging.info('There is no such directory, I am creating it...')
        os.makedirs(path)
        logging.info('The creation of the directory is completed.')
    elif not autocreate and not path_exists:
        text_error = f'The directory [{path}] does not exist and autocreate is False!'
        raise RuntimeError(text_error)

    # Change directory.
    os.chdir(path)

    logging.info(f'Changing the current application directory to [{path}] is completed.')


def get_files() -> list:
    """Get info about all files in working directory.

    Returns:
        List of dicts, which contains info about each file. Keys:
        - name (str): filename
        - create_date (datetime): date of file creation.
        - edit_date (datetime): date of last file modification.
        - size (int): size of file in bytes.
    """
    logging.info('Getting info about all files in working directory...')

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

    logging.info('Getting info about all files in working directory is completed.')
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
    logging.info(f'Getting full info about file [{filename}]...')

    with open(filename, 'rb') as file:
        data = file.read()

    # The content must be returned in a string representation. I try utf-8 first, then ANSI.
    try:
        data = data.decode()
    except Exception:
        data = data.decode('ANSI')

    file_info = {
        'name': os.path.split(filename)[-1],
        'content': data,
        'create_date': time.ctime(os.path.getctime(filename)),
        'edit_date': time.ctime(os.path.getmtime(filename)),
        'size': os.path.getsize(filename)
    }

    logging.info(f'Getting full info about file [{filename}] is completed.')
    return file_info


def create_file(filename: str, content: bytes = None) -> dict:
    """Create a new file.

    Args:
        filename (str): Filename.
        content (bytes): Bytes with file content.

    Returns:
        Dict, which contains name of created file. Keys:
        - name (str): filename
        - content (str): file content
        - create_date (datetime): date of file creation
        - size (int): size of file in bytes

    Raises:
        ValueError: if filename is invalid.
    """
    logging.info(f'Creating a file [{filename}] with content...')

    # Checking the file for validity.
    __checking_path(filename)

    # Create file.
    with open(filename, 'wb') as file:
        if content:
            # data = bytes(content)
            file.write(content)

    return get_file_data(filename)

    logging.info(f'Creating a file [{filename}] with content is completed.')


def delete_obj(path: str) -> None:
    """Delete file|directory.

    Args:
        path (str): path to filename or directory.

    Returns:
        obj_name if the file|directory was successfully deleted.

    Raises:
        RuntimeError: if path does not exist.
        ValueError: if path is invalid.
    """
    logging.info(f'Deleting [{path}]...')

    # Checking a file.
    __checking_path(path)
    if not os.path.exists(path):
        raise RuntimeError(f'[{path}] does not exist!')

    # Deleting file.
    if os.path.isfile(path):
        obj_name = 'file'
        os.remove(path)
    # Deleting directory.
    else:
        obj_name = 'directory'
        rmtree(path)

    if not os.path.exists(path):
        logging.info(f'Deleting a {obj_name} [{path}] is completed.')
        return obj_name
    else:
        raise RuntimeError(f'{obj_name.capitalize()} {path} could not be deleted!')
