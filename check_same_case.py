def same_case(a, b):

    if a == b:
        return 1
    elif (a == int) or (b == int):
        return -1
    elif (a is str) or (b is not str) and (a is not str) or (b is str):
        return 0

print(same_case(1,"hola"))
