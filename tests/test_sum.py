from apps.sum import add

def test_add():

    assert add(9,6) == 15
    print("-----------------------test passed successfully-----------------------")


if __name__ == "__main__":

    test_add()