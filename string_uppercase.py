def is_uppercase(inp):
    frase = inp.upper()

    if inp != frase:
        return False
    else:
        return True

print(is_uppercase("hola"))
