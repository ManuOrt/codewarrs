def duplicate_encode(word):
    encoded = ''
    word = word.lower()

    for char in word:
        if word.count(char) > 1:
            encoded += ")"
        else:
            encoded += "("

    return encoded


if __name__ == '__main__':
    assert (duplicate_encode("din")) == "((("
    assert (duplicate_encode("recede")) == "()()()"
    assert (duplicate_encode("Success")) == ")())())"
    assert (duplicate_encode("(( @")) == "))(("
