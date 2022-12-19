import codewars_test as test
def area_or_perimeter(l , w):

    if l == w:
        cuadrado = l * w
        return cuadrado
    elif l != w:
        rectangulo = l + l + w + w
        return rectangulo




test.assert_equals(area_or_perimeter(4, 4), 16)
test.assert_equals(area_or_perimeter(6, 10), 32)