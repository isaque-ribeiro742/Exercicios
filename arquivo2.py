def gerar_boletim(notas):
    m=[]
    for linha in notas:
        dados = linha.strip().split(',')
        m.append(dados)
        for coluna in range(2):
                m[-1][1+coluna]=float(m[-1][1+coluna])
    return m
with open("notas_brutas.txt", "r", encoding="utf-8") as notas, open("boletim_oficial.txt", "w",) as boletim:             
    notas=gerar_boletim(notas)
    for notas in notas:
         media=(notas[1]+notas[2])/2
         if media >=70:
              boletim.write(f"nome:{notas[0]}, media: {media} , aprovado\n")
         else :
                 boletim.write(f"nome:{notas[0]}, media: {media} , reprovado\n")