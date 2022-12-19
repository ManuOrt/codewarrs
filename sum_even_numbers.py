def sum_even_numbers(seq):
    resultado = 0
    s = [str(num) for num in seq]
    if num%2 == 0:
        resultado = num + resultado
        resultado = ''.join(s)
        return int(resultado)




