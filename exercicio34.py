while True:
    texto=input("digite uma palavra :")
    if texto==texto[::-1]:
        print(f"{texto} , essa palavra e um palidromo")
    else:
        print(f"{texto} , essa  nao e um palidromo")   