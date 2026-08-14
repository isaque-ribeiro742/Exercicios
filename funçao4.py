def inverter_numero(n):
    numero_positivo = n * -1
    if n < 0 :
      invertida=str(numero_positivo)[::-1]
      return int(invertida)*-1
    else:  
       invertida=str(numero_positivo )[::-1]
    return int(invertida)
n=-189
print(inverter_numero(n))

