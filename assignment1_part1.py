class ListDivideException(Exception):
    pass


def listDivide(numbers, divide=2):
    res = 0
    for i in numbers:
        if i % divide == 0:
            res += 1
    return res


def testListDivide():
    try:
        assert listDivide([1, 2, 3, 4, 5]) == 2, "Should return 2"
        assert listDivide([2, 4, 6, 8, 10]) == 5, "Should return 5"
        assert listDivide([30, 54, 63, 98, 100], divide=10) == 2, "Should return 2"
        assert listDivide([]) == 0, "Should return 0"
        assert listDivide([1, 2, 3, 4, 5], 1) == 5, "Should return 5"
    except ListDivideException:
        print("Could Not Divide Any Number")


testListDivide()
