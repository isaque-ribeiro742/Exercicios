def calcular_media(notas):
    media=sum (notas)/len(notas)
    if media < 7 and media >= 5 :
        return 'recuperaçao'
    elif media < 5 :
        return 'reprovado'
    else:
        return 'aprovado'
notas=[]
while True:
    nota=float(input("digite a nota ou 0 quando nao tever mais notas")) 
    if nota ==0 and len(notas) == 0:
        print("nao a notas ainda")
        continue
    if nota != 0:
        notas.append(nota)
    else:
        break
print(calcular_media(notas))        

    
