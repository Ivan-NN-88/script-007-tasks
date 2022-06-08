import a


def b_const():
    return a.A_CONSTANT * 2


def b_func():
    return a.a_func() * 3


def b_class():
    aobj = a.AClass()
    return aobj.do_something() * 4
