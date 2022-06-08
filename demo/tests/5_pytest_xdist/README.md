
# Определение длительности тестов

Медленные тесты можно определить с помощью параметра `--durations`:

```console
$ pytest --help | grep durations
  --durations=N         show N slowest setup/test durations (N=0 for all).
  --durations-min=N     Minimal duration in seconds for inclusion in slowest

$ pytest --durations=0
...
===================== slowest durations =====================
2.01s call     demo/tests/5_pytest_xdist/test_slow.py::test_slow
0.01s setup    demo/tests/2_pytest_tmp_path/test_tmp_path.py::test_create_file

(145 durations < 0.005s hidden.  Use -vv to show these durations.)
==== 45 passed, 4 skipped, 1 xfailed, 1 warning in 2.29s ====
```

Чтобы увидеть информацию детальную информацию, воспользуйтесь командой:

```console
$ pytest --durations=0 -vv
...
===================== slowest durations =====================
2.00s call     demo/tests/5_pytest_xdist/test_slow.py::test_slow
0.02s setup    demo/tests/2_pytest_tmp_path/test_tmp_path.py::test_create_file
0.00s teardown demo/tests/1_pytest/test_09_conftest.py::TestCheckFile::test_existent
...
```

# Параллельное выполнение тестов

Пакет [`pytest-xdist`](https://pytest-xdist.readthedocs.io/en/latest/) позволяет запускать тесты параллельно:

```console
$ pytest -n auto
$ pytest -n 3
```

Из-за особенностей реализации параметр `-s/--capture` не работает.
