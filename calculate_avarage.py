import codewars_test as test

def find_average(numbers):
    resultado = 0
    for enum in numbers:
        resultado += enum
    resultado_final = resultado / len(numbers)
    return resultado_final



test.assert_equals(find_average([1, 2, 3]), 2)