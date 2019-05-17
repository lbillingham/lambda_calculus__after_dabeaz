ZERO = lambda f: lambda x: x  # same as FALSE
ONE = lambda f: lambda x: f(x)
TWO = lambda f: lambda x: f(f(x))
THREE = lambda f: lambda x: f(f(f(x)))
FOUR = lambda f: lambda x: f(f(f(f(x))))
FIVE = lambda f: lambda x: f(f(f(f(f(x)))))


SUCC = lambda n: (lambda f: lambda x: f(n(f)(x)))

ADD = lambda n: lambda m: n(SUCC)(m)

MUL = lambda n: lambda m: lambda f: m(n(f))
