def palidromo(texto):
    texto=texto.replace(" ","").lower()
    if len(texto) <=1:
        return True
    elif texto[0]==texto[-1]:
        return palidromo(texto[1:-1])
    else:
        return False
if palidromo("osso e isso"):
    print("e um palidromo")    
else:
    print("nao e um palidromo")    