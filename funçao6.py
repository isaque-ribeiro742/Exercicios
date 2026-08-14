def calcular_media(n1,n2):
    media=(n1+n2)/2
    return media
def  verificar_situacao(nome,n1,n2):
    media=calcular_media(n1,n2)
    print(f'nome : {nome} | {media}')
    if media >= 70:
        print("situaçao: aprovado")
    elif media >=40 and media < 70:
        print("situaçao: prova final")
    else:
        print("situaçao: reprovado")        
verificar_situacao("isaque",100,100)
verificar_situacao("carlos",0,100)
verificar_situacao("pai",40,30)

