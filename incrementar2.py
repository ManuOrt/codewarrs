import codewars_test as test


def incrementer(nums):






test.assert_equals(incrementer([]), [])
test.assert_equals(incrementer([1, 2, 3]), [2, 4, 6])
test.assert_equals(incrementer([4, 6, 7, 1, 3]), [5, 8, 0, 5, 8])
test.assert_equals(incrementer([3, 6, 9, 8, 9]), [4, 8, 2, 2, 4])
test.assert_equals(incrementer([1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 9, 9, 8]),[2, 4, 6, 8, 0, 2, 4, 6, 8, 9, 0, 1, 2, 2])