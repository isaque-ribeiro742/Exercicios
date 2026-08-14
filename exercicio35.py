while True:
    texto=input("digite uma frase :")
    texto=texto.replace(" ","")
    if texto==texto[::-1]:
        print(f"{texto}, essa palavra e um palidromo")
    else:
        print(f"{texto}, essa palavra nao e um palidromo")   