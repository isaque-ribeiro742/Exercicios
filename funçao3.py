def filtrar_positivos(lista_numeros):
    lista_positiva=[]
    for i in lista_numeros:
        if i > 0:
            lista_positiva.append(i)
    return lista_positiva
lista_numeros=[-1,9,0,-9,10,]
print(filtrar_positivos(lista_numeros))
