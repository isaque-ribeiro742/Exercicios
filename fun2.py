def contar_vogais(texto):
    if len(texto)==0:
        return 0
    if texto[0] in "aeiou":
        return 1+  contar_vogais(texto[1:])
    else:
        return contar_vogais(texto[1:])
print(contar_vogais("aeiou"))   