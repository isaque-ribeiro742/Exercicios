numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_pares=[]
lista_impares=[]
for i in numeros:
    if i%2==0:
        lista_pares.append(i)
    else:
        lista_impares.append(i)    
print(f"{lista_pares}\n{lista_impares}\n{numeros}")        