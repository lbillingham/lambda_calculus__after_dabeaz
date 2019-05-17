import pytest

from numbers_kinda import ZERO, ONE, TWO, THREE, FOUR, FIVE
from numbers_kinda import ADD, MUL
from numbers_kinda import SUCC

incr = lambda x: x + 1
show = lambda fun: fun(incr)(0)


def test_setup():
    assert incr(0) == 1
    assert incr(999) == 1000


@pytest.mark.parametrize(
    "num_fun, expected",
    [(ZERO, 0), (ONE, 1), (TWO, 2), (THREE, 3), (FOUR, 4), (FIVE, 5)],
)
def test_nums_with_incr(num_fun, expected):
    assert show(num_fun) == expected


@pytest.mark.parametrize(
    "num_fun0, num_fun1, expected",
    [
        (ZERO, ONE, 0),
        (ONE, ZERO, 0),
        (FOUR, THREE, 81),
        (THREE, FOUR, 63),
        (ONE, TWO, 2),
        (TWO, TWO, 4),
        (THREE, TWO, 8),
        (FOUR, TWO, 16),
        (FIVE, TWO, 32),
    ],
)
def combining_is_pow(num_fun0, num_fun1, expected):
    assert show(num_fun0(num_fun1)) == expected


@pytest.mark.parametrize(
    "num_fun, expected", [(ZERO, 1), (ONE, 2), (TWO, 3), (THREE, 4), (FOUR, 5)]
)
def test_single_SUCC(num_fun, expected):
    assert show(SUCC(num_fun)) == expected


def test_repeated_SUCC():
    assert show(SUCC(SUCC(SUCC(SUCC(SUCC(ZERO)))))) == 5


@pytest.mark.parametrize(
    "num_fun0, num_fun1, expected",
    [
        (ONE, TWO, 2),
        (TWO, ONE, 2),
        (TWO, TWO, 4),
        (TWO, THREE, 6),
        (ZERO, ONE, 0),
        (ONE, ZERO, 0),
        (FOUR, THREE, 12),
        (THREE, FOUR, 12),
        (ONE, TWO, 2),
        (TWO, TWO, 4),
        (THREE, TWO, 6),
        (FOUR, TWO, 8),
        (FIVE, TWO, 10),
    ],
)
def test_MUL(num_fun0, num_fun1, expected):
    assert show(MUL(num_fun0)(num_fun1)) == expected


@pytest.mark.parametrize(
    "num_fun0, num_fun1, expected",
    [
        (ZERO, ONE, 1),
        (ONE, ZERO, 1),
        (FOUR, THREE, 7),
        (THREE, FOUR, 7),
        (ONE, TWO, 3),
        (TWO, TWO, 4),
        (THREE, TWO, 5),
        (FOUR, TWO, 6),
        (FIVE, TWO, 7),
    ],
)
def test_ADD(num_fun0, num_fun1, expected):
    assert show(ADD(num_fun0)(num_fun1)) == expected
