from fun4 import verificar_palindromo
with open('tentativas.txt','r',encoding='utf-8')as senha,open("cofre_seguro.txt","a")as cofre:
    for linha in senha:
        linha=str(linha)
        linha=linha.strip()
        if verificar_palindromo(linha)==True:
         cofre.write(linha+"\n")
            