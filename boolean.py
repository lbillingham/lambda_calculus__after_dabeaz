def TRUE(x):
    """same as
        - `TRUE = lambda x: lambda y: x`
        - `switch.LEFT`
    """
    return lambda y: x


def FALSE(x):
    """same as
        - `FALSE = lambda x: lambda y: y`
        - `switch.RIGHT`
    """
    return lambda y: y


def NOT(x):
    return x(FALSE)(TRUE)


def AND(x):
    """same as
        - return lambda y: x(y)(x)
    """
    # could also x(y)(x)
    return lambda y: x(y)(FALSE)


def OR(x):
    return lambda y: x(x)(y)
