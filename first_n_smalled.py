import codewars_test as test


def first_n_smallest(arr, n):
    result = []

    arr_sorted = sorted(arr)
    arr_chopped = arr_sorted[:n]

    for ele in arr:
        if ele in arr_chopped:
            result.append(ele)
            arr_chopped.remove(ele)

    return result


test.describe("Basic tests")
test.assert_equals(first_n_smallest([1, 2, 3, 4, 5], 3), [1, 2, 3])
test.assert_equals(first_n_smallest([5, 4, 3, 2, 1], 3), [3, 2, 1])
test.assert_equals(first_n_smallest([1, 2, 3, 1, 2], 3), [1, 2, 1])
test.assert_equals(first_n_smallest([1, 2, 3, -4, 0], 3), [1, -4, 0])
test.assert_equals(first_n_smallest([1, 2, 3, 4, 5], 0), [])
test.assert_equals(first_n_smallest([1, 2, 3, 4, 5], 5), [1, 2, 3, 4, 5])
test.assert_equals(first_n_smallest([1, 2, 3, 4, 2], 4), [1, 2, 3, 2])
test.assert_equals(first_n_smallest([2, 1, 2, 3, 4, 2], 2), [2, 1])
test.assert_equals(first_n_smallest([2, 1, 2, 3, 4, 2], 3), [2, 1, 2])
test.assert_equals(first_n_smallest([2, 1, 2, 3, 4, 2], 4), [2, 1, 2, 2])
test.assert_equals(first_n_smallest([-8, -10, -3, -10, 2, -10, -9, 5, 7, 9, -1, 7, 2, -1, -5, 8, 0], 11), [-8, -10, -3, -10, 2, -10, -9, -1, -1, -5, 0])
print("<COMPLETEDIN::>")
