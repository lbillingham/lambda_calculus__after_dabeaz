def TRUE(x):
    return lambda y: x


def FALSE(x):
    return lambda y: y


def NOT(x):
    return x(FALSE)(TRUE)


def AND(x):
    # could also x(y)(x)
    return lambda y: x(y)(FALSE)


def OR(x):
    return lambda y: x(x)(y)
