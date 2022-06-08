import os

import pytest

from server import FileService


@pytest.mark.parametrize('value', [None, 1])
def test_incorrect_type(value, test_dir):
    """Передать значения неподходящих типов

    Ожидаемый результат: возбуждение исключения TypeError
    """
    with pytest.raises(TypeError):
        FileService.change_dir(value)


def test_dot_dir(test_dir):
    """Передать . в качестве значения,

    Ожидаемый результат: текущая папка не должна измениться
    """
    old_cwd = os.getcwd()
    FileService.change_dir('.')
    assert old_cwd == os.getcwd()


@pytest.mark.parametrize('value', ['..', '../something'])
def test_incorrect_value(value, test_dir):
    """Передать некорректные значения

    Ожидаемый результат: возбуждение исключения ValueError
    """
    with pytest.raises(ValueError):
        FileService.change_dir(value)


def test_existing_dir_no_create(test_dir):
    """Перейти в каталог, который уже существует и autocreate=False

    Ожидаемый результат: текущая папка имеет имя ExistingDirectory
    """
    os.mkdir('ExistingDirectory')
    FileService.change_dir('ExistingDirectory', autocreate=False)
    cwd = os.getcwd()
    assert os.path.basename(cwd) == 'ExistingDirectory'


def test_existing_dir_create(test_dir):
    """Перейти в каталог, который уже существует и autocreate=True

    Ожидаемый результат: текущая папка имеет имя ExistingDirectory
    """
    os.mkdir('ExistingDirectory')
    FileService.change_dir('ExistingDirectory', autocreate=True)
    cwd = os.getcwd()
    assert os.path.basename(cwd) == 'ExistingDirectory'


def test_non_existing_dir_no_create(test_dir):
    """Перейти в каталог, который не существует и autocreate=False

    Ожидаемый результат: текущая папка имеет имя отличное от NotExistingDirectory
    """
    with pytest.raises(RuntimeError):
        FileService.change_dir('NotExistingDirectory', autocreate=False)
    cwd = os.getcwd()
    assert os.path.basename(cwd) != 'NotExistingDirectory'


def test_non_existing_dir_create(test_dir):
    """Перейти в каталог, который не существует и autocreate=True

    Ожидаемый результат: текущая папка имеет имя отличное от NotExistingDirectory
    """
    FileService.change_dir('NotExistingDirectory', autocreate=True)
    cwd = os.getcwd()
    assert os.path.basename(cwd) == 'NotExistingDirectory'
