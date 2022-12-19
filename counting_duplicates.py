import codewars_test as test


def duplicate_count(text):
    text = text.lower()
    count = {i: text.count(i) for i in set(text)}
    count = sorted(count.values())
    result = 0
    for i in count:
        if i > 1:
            result += 1
    return result

'''def duplicate_count(text):
    text = text.lower()
    duplicates = []
    for i in text:
        if text.count(i) > 1 and i not in duplicates:
            duplicates.append(i)    
    return len(duplicates)'''











test.assert_equals(duplicate_count(""), 0)
test.assert_equals(duplicate_count("abcde"), 0)
test.assert_equals(duplicate_count("abcdeaa"), 1)
test.assert_equals(duplicate_count("abcdeaB"), 2)
test.assert_equals(duplicate_count("Indivisibilities"), 2)