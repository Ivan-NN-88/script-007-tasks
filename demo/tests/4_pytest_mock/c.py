from a import A_CONSTANT, a_func, AClass


def c_const():
    return A_CONSTANT * 2


def c_func():
    return a_func() * 3


def c_class():
    a = AClass()
    return a.do_something() * 4
