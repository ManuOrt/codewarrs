import codewars_test as test

def summation(num):
    total = 0
    for numero in range(0, num+1):
        total = total + numero
    return total






test.assert_equals(summation(1), 1)
test.assert_equals(summation(8), 36)
test.assert_equals(summation(22), 253)
test.assert_equals(summation(100), 5050)
test.assert_equals(summation(213), 22791)
