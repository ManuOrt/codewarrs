import codewars_test as test


def find_uniq(arr):
    order = sorted(arr)
    if order[0] != order[1]:
        return order[0]
    else:
        return order[-1]











test.assert_equals(find_uniq([1, 1, 1, 2, 1, 1]), 2)
test.assert_equals(find_uniq([0, 0, 0.55, 0, 0]), 0.55)
test.assert_equals(find_uniq([3, 10, 3, 3, 3]), 10)