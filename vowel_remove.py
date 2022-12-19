import codewars_test as test

def shortcut(s):
    vowels = ('a', 'e', 'i', 'o', 'u')
    result = ''

    for letter in s:
        if letter not in vowels:
            result += letter
    return result








test.assert_equals(shortcut('hello'), 'hll')