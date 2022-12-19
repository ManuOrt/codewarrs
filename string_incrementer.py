import codewars_test as test


def increment_string(strng):
    # strip the decimals from the right
    stripped = strng.rstrip('1234567890')

    # get the part of strng that was stripped
    ints = strng[len(stripped):]

    if len(ints) == 0:
        return strng + '1'
    else:
        # find the length of ints
        length = len(ints)

        # add 1 to ints
        new_ints = 1 + int(ints)

        # pad new_ints with zeroes on the left
        new_ints = str(new_ints).zfill(length)

        return stripped + new_ints





test.assert_equals(increment_string("foo"), "foo1")
test.assert_equals(increment_string("foobar001"), "foobar002")
test.assert_equals(increment_string("foobar1"), "foobar2")
test.assert_equals(increment_string("foobar00"), "foobar01")
test.assert_equals(increment_string("foobar99"), "foobar100")
test.assert_equals(increment_string("foobar099"), "foobar100")
test.assert_equals(increment_string("fo99obar99"), "fo99obar100")
test.assert_equals(increment_string(""), "1")