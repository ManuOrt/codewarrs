import codewars_test as test

def wave(people):
    result = []
    for letter in people:
        letter = letter.upper()
        result = letter + people[1:]
    return wave("hola")










