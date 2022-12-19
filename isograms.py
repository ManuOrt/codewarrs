import codewars_test as test


def is_isogram(string):
    repetidas = 0
    if string == "":
        return True, "an empty string is a valid isogram"
    for letter in string:
        if letter.count(letter) > 1:
            repetidas += 1
            return False, "same chars may not be adjacent"
        else:
            return True





test.assert_equals(is_isogram("Dermatoglyphics"), True)
test.assert_equals(is_isogram("isogram"), True)
test.assert_equals(is_isogram("aba"), False, "same chars may not be adjacent")
test.assert_equals(is_isogram("moOse"), False, "same chars may not be same case")
test.assert_equals(is_isogram("isIsogram"), False)
test.assert_equals(is_isogram(""), True, "an empty string is a valid isogram")