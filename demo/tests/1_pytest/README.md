
# Documentation

https://docs.pytest.org/en/latest/getting-started.html

Перевод на русский:
https://pytest-docs-ru.readthedocs.io/ru/latest/contents.html

[Naming conventions](https://docs.pytest.org/en/latest/reference.html#confval-python_classes):

- files matching `test_*.py` and `*_test.py` will be considered test modules
- class names must start with `Test` and miss the `__init__` method
- pytest will consider any function prefixed with `test` as a test
- test folder must contain `__init__.py` file (usually empty)

Фикстуры для пропуска тестов или отметки их упавшими:
https://pytest-docs-ru.readthedocs.io/ru/latest/skipping.html

# Run tests

Usage:

```console
$ pytest [options] [file_or_dir] [file_or_dir] [...]
```

For example:

```console
$ pytest demo/tests/mypytests
$ pytest demo/tests/mypytests/test_01_assert.py
```

# Capture output

https://docs.pytest.org/en/latest/capture.html

Extra summary info can be shown using the '-r' option:

```console
$ pytest --help | rg -e -r -C 3
  -r chars              show extra test summary info as specified by chars:
                        (f)ailed, (E)rror, (s)kipped, (x)failed, (X)passed,
                        (p)assed, (P)assed with output, (a)ll except passed
                        (p/P), or (A)ll. Warnings are displayed at all times
```

shows the captured output of passed tests:

```console
$ pytest -rP
```

shows the captured output of failed tests (default behaviour):

```console
$ pytest -rx
```

`-s` allows seeing output as is.

## Ignore tests in some folders

```console
$ pytest --ignore=1 --ignore=demo
```

## Run only specific tests

```console
$ pytest -k part_of_name
```

or

```console
$ pytest test_FileService.TestChangeDir.test_incorrect_value3
```
