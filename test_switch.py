from switch import LEFT, RIGHT


def test_LEFT():
    assert LEFT("5v")("grnd") == "5v"


def test_RIGHT():
    assert RIGHT("5v")("grnd") == "grnd"
