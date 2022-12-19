import codewars_test as test
def past(h, m, s):
    result = 0
    if h == 1:
        result = result + 3600000
    if h > 1:
        result = h * 3600000 + result
    if m == 1:
        result = result + 60000
    if m > 1:
        result = m * 60000 + result
    if s == 1:
        result = result + 1000
    if s > 1:
        result = s * 1000 + result
    return result

#def past(h, m, s):
    #return 3600000 * h + 60000 * m + 1000 * s



test.assert_equals(past(0, 1, 1), 61000)
test.assert_equals(past(1, 1, 1), 3661000)
test.assert_equals(past(0, 0, 0), 0)
test.assert_equals(past(1, 0, 1), 3601000)
test.assert_equals(past(1, 0, 0), 3600000)