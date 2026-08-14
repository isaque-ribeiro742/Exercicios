maratona=[]
while True:
    nome=input("digite o nome da equipe ou fim para encerrar o progama : ")
    if nome =="fim" and len(maratona)==0:
        print("nao a equipes ainda")
        continue
    if nome =="fim" :
        break
    else:
        poblema=int(input("poblemas resolvidos : "))
        maratona.append(([nome,poblema]))
print("="*30)
print("DESEMPENHO NA MARATONA")
print("="*30)
for i in range (len(maratona)):
    e="*"*maratona[i][1]
    print(f"{maratona[i][0]}  |  {e} ")
    