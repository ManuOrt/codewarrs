def xo(s):
    resultado_x = 0
    resultado_o = 0

    for item in s.lower():
        if item == 'x':
            resultado_x += 1
        elif item == 'o':
            resultado_o += 1
    if resultado_x == resultado_o:
        return True
    else:
        return False

'''  Otras maneras de hacerlo
    def xo(s):
        s = s.lower()
        return s.count('x') == s.count('o')'''