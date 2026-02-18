from calc import add

def test_add():
    # This will fail when 2 + 3 != 6
    assert add(2, 3) == 6

if __name__ == "__main__":
    test_add()
