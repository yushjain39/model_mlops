from apps.sum import add, sub

def test_add():

    assert add(9,6) == 15
    print("-----------------------test passed successfully-----------------------")
def test_sub():
    
    assert sub(9,6) == 3

if __name__ == "__main__":

    test_add()