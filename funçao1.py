def es_palindromo(texto):
    if texto[:] == texto[::-1]:
        return True
    else:
        return False
texto=(input("digite um nome :")).lower ()   
es_palindromo(texto)
r=es_palindromo(texto)
print(r)
       
