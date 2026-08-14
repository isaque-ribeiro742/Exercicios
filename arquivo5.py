def criar(m=[]):
   with open("grafico_maratona.txt","a") as grafico:
      for i in range(len(m)):
         barra=m[i][1]*"*"
         grafico.write(f"{m[i][0]}/{barra}\n")
criar(m=[["Alpha", 5],["Beta", 4],["Gama", 4],["Delta", 5],["Epsilon", 7]])         