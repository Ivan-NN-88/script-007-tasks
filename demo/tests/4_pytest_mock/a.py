import time

A_CONSTANT = 1


def a_func():
    time.sleep(5)
    return 2


class AClass:

    def __init__(self):
        self.data = None

    def do_something(self):
        time.sleep(5)
        self.data = 3
