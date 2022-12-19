import codewars_test as test


def to_float_array(arr):
    return([float(x) for x in arr])


test.assert_equals(to_float_array(["1.1", "2.2", "3.3"]), [1.1, 2.2, 3.3])