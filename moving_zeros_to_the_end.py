import codewars_test as test

def move_zeros(lst):
    numero_ocurrencias = lst.count(0)
    lista_zeros = 0

    while lista_zeros < numero_ocurrencias:
        lista_zeros += 1
        lst.remove(0)
        lst.append(0)
    return lst



test.assert_equals(move_zeros(
[1, 2, 0, 1, 0, 1, 0, 3, 0, 1]),
[1, 2, 1, 1, 3, 1, 0, 0, 0, 0])
test.assert_equals(move_zeros(
[9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]),
[9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
test.assert_equals(move_zeros([0, 0]), [0, 0])
test.assert_equals(move_zeros([0]), [0])
test.assert_equals(move_zeros([]), [])