import codewars_test as test

def sum_of_differences(arr):
    resultado = []
    ordenar = arr.sort()







test.assert_equals(sum_of_differences([1, 2, 10]), 9)
test.assert_equals(sum_of_differences([-3, -2, -1]), 2)
test.assert_equals(sum_of_differences([1, 1, 1, 1, 1]), 0)
test.assert_equals(sum_of_differences([-17, 17]), 34)
test.assert_equals(sum_of_differences([]), 0)
test.assert_equals(sum_of_differences([0]), 0)
test.assert_equals(sum_of_differences([-1]), 0)
test.assert_equals(sum_of_differences([1]), 0)