def palidromo(texto):
    texto=texto.replace(" ","")
    if len(texto) <=1: 
        return True
    elif texto[0]==texto[-1]:
        return palidromo(texto[1:-1])
    
if palidromo("oss")==True:
    print("palidromo")
else:
    print("nao e um palidromo")  