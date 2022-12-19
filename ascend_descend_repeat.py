import codewars_test as test
from math import ceil

def ascend_descend(size,s,e):
    lst = [*range(s, e+1)]
    lst += lst[-2:0:-1]
    s = ''.join(map(str, lst))
    return s and (s * ceil(size/len(s)))[:size]




test.assert_equals(ascend_descend(5, 1, 3), "12321")
test.assert_equals(ascend_descend(14, 0, 2), "01210121012101")
test.assert_equals(ascend_descend(11, 5, 9), "56789876567")