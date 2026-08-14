m=[['','',''],
   ['','',''],
   ['','','']]
def exibir_tabuleiro(m):
    for linha in range(len(m)):
        for coluna in range(len(m)):
            if coluna <=1:
                print(f"{m[linha][coluna]}   |",end="")
            else:
                print(f"{m[linha][coluna]}")        
        if linha <=1 :        
            print("---+---+---")
while True:
    xlinha=int(input("digite o indicir da linha que vc que colocar  x :") )
    xcoluna=int(input("digite o indicir da coluna que vc que colocar  x :") )
    m[xlinha][xcoluna]="x"
    exibir_tabuleiro(m)
    olinha=int(input("digite o indicir da linha que vc que colocar o :") )
    ocoluna=int(input("digite o indicir da coluna que vc que colocar o  :") )
    m[olinha][ocoluna]="o"
    exibir_tabuleiro(m)
    fim=input("digite 1 se que acabar a partida ou 0 pra continuar")
    if fim =="1":
        break
exibir_tabuleiro(m)                    