import math
import codewars_test as test


def cockroach_speed(s):
    cm = s * 27.777777777778
    resultado = math.floor(cm)
    return resultado







test.assert_equals(cockroach_speed(1.08),30)
test.assert_equals(cockroach_speed(1.09),30)
test.assert_equals(cockroach_speed(0),0)