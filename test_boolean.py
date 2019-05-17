from boolean import AND, FALSE, NOT, OR, TRUE


def test_TRUE():
    assert TRUE("lefty")("righty") == "lefty"


def test_FALSE():
    assert FALSE("lefty")("righty") == "righty"


def test_NOT_inverts_TRUE():
    assert NOT(TRUE) == FALSE


def test_NOT_inverts_FALSE():
    assert NOT(FALSE) == TRUE


def test_AND_TT():
    assert AND(TRUE)(TRUE) == TRUE


def test_AND_FF():
    assert AND(FALSE)(FALSE) == FALSE


def test_AND_TF():
    assert AND(TRUE)(FALSE) == FALSE


def test_AND_FT():
    assert AND(FALSE)(TRUE) == FALSE


def test_OR_TT():
    assert OR(TRUE)(TRUE) == TRUE


def test_OR_FF():
    assert OR(FALSE)(FALSE) == FALSE


def test_OR_TF():
    assert OR(TRUE)(FALSE) == TRUE


def test_OR_FT():
    assert OR(FALSE)(TRUE) == TRUE
