def sum_even_numbers(seq):
    resultado = 0
    for enum in seq:
        if enum%2 == 0:
            resultado += enum
    return resultado

