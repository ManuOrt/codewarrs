import codewars_test as test


def get_real_floor(n):

    if n < 13 or n == 0:
        return n -1
    elif n > 13:
        return n -2
    elif n < 0:
        return n






test.assert_equals(get_real_floor(1), 0)
test.assert_equals(get_real_floor(5), 4)
test.assert_equals(get_real_floor(15), 13)
test.assert_equals(get_real_floor(-421), -420)