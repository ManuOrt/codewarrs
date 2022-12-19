import codewars_test as test
from string import ascii_lowercase

def is_pangram(s):
    min = s.lower()
    if set(s) >= set(ascii_lowercase):
        return True
    else:
        return False



test.assert_equals(is_pangram("The quick, brown fox jumps over the lazy dog!"), True)
test.assert_equals(is_pangram("1bcdefghijklmnopqrstuvwxyz"), False)