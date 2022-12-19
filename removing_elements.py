import codewars_test as test

def remove_every_other(my_list):
    contador = 0
    mi_lista = []
    for ele in my_list:
        if contador%2 == 0:
            mi_lista.append(ele)
            contador += 1
        else:
            contador += 1
    return mi_lista


test.assert_equals(remove_every_other(['Hello', 'Goodbye', 'Hello Again']),
['Hello', 'Hello Again'])
test.assert_equals(remove_every_other([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
[1, 3, 5, 7, 9])
test.assert_equals(remove_every_other([[1, 2]]), [[1, 2]])
test.assert_equals(remove_every_other([['Goodbye'], {'Great': 'Job'}]),
[['Goodbye']])