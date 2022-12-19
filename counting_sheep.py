def count_sheeps(sheep):
    contador = 0
    for item in sheep:
        if item == True:
            contador += 1
    return contador




array1 = [True,  True,  True,  False,
          True,  True,  True,  True ,
          True,  False, True,  False,
          True,  False, False, True ,
          True,  True,  True,  True ,
          False, False, True,  True ];

assert count_sheeps(array1) == 17

print(count_sheeps(array1))