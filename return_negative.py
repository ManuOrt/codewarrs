import codewars_test as test

def make_negative( number ):

    if number == 0:
        return number
    elif number < 0:
        return number
    elif number > 0:
        number = - number
        return number



for n, expected in ((42,-42), (-9,-9), (0,0)):
            actual = make_negative(n)
            message = f"For n = {n}, expected {expected} but got {actual}"
            test.assert_equals(actual, expected, message)