from add import add


# function based tests.
def test_add():
    assert add(1, 2) == 3


# class based testing.
class TestAdd:

    def test_add(self):
        assert add(1, 2) == 3
