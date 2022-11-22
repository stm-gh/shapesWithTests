from add import add, subtract


# function based tests.
def test_add():
    assert add(1, 2) == 3

def test_subtract():
    assert subtract(-1,-3) == 2
