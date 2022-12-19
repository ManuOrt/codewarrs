def comp(array1, array2):
    if (array1 is None and not array2) or (array2 is None and not array1):
        return False
    elif len(array1) != len(array2):
        return False

    for num in array1:
        if num**2 in array2:
            array2.remove(num**2)
        else:
            return False
    return True



'''longitud = len(array1)
    for num in range(longitud):
        array1[longitud - num - 1]
        num = num**2
        numero_veces = array2.count(num)
        if numero_veces == 0:
            return False
        return True'''

if __name__ == "__main__":
    print("Bateria de test basicos")
a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
assert comp(a1, a2) == True
a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*21, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
assert comp(a1, a2) == False
a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*11, 121*121, 144*144, 190*190, 161*161, 19*19, 144*144, 19*19]
assert comp(a1, a2) == False