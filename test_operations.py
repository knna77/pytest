import operations


def test_suma():
    assert operations.suma(1, 1) == 2
    assert operations.suma(1, 5) == 6
    assert operations.suma(1, -1) == 0
    assert operations.suma(0, 8) == 8


def test_resta():
    assert operations.resta(1, 1) == 0
    assert operations.resta(1, 5) == -4
    assert operations.resta(9, 3) == 6
    assert operations.resta(3, 9) == -6


def test_mult():
    assert operations.mult(0, 1) == 0
    assert operations.mult(5, 5) == 25
    assert operations.mult(4, -4) == -16
    assert operations.mult(1, 0) == 0


def test_div():
    assert operations.div(1, 1) == 1
