def LEFT(a):
    def f(b):
        return a

    return f


def RIGHT(a):
    def f(b):
        return b

    return f
