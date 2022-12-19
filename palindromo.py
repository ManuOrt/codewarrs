def permute_a_palindrome (input):
    if str(input) == str(input)[::-1]:
        return True #Si leido desde izquierda a derecha es igual a derecha izquierda
    first = input[1:] + input[0] #Creamos una variable nueva que ponga la segunda posicion en la primera
    if str(first) == str(first)[::-1]: #Si al cambiar la primera posicion por la ultima, se le igual normal y del reves return true
        return True
    last = input[-1] + input[0:-1] # Cambia la primera posicion por la segunda
    if str(last) == str(last)[::-1]:
        return True
    return False








if __name__ == "__main__":
    print("Bateria de test basicos")
assert permute_a_palindrome("a") == True
assert permute_a_palindrome("aa") == True
assert permute_a_palindrome("baa") == True
assert permute_a_palindrome("aab") == True
assert permute_a_palindrome("baabcd") == False
assert permute_a_palindrome("racecars") == False
#prueba assert permute_a_palindrome("aaaaaab") == True
    
assert permute_a_palindrome("abcdefghba") == False
assert permute_a_palindrome("") == True