import codewars_test as test

def enough(cap, on, wait):
    if wait - (cap-on) < wait:
        return wait - (cap-on)
    else:
        return 0

    '''def enough(cap, on, wait):
        return wait - (cap - on) if (cap - on) < wait else 0'''



test.assert_equals(enough(10, 5, 5), 0)
test.assert_equals(enough(100, 60, 50), 10)
test.assert_equals(enough(92, 64, 57), 29)