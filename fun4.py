def verificar_palindromo(texto):
    texto=texto.replace(" ","").lower()
    if len(texto)<=1:
        return True
    elif texto[0]==texto[-1] :
        return verificar_palindromo(texto[1:-1])
    else :
           return False
    


