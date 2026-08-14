def rotacionar(matriz=[]):
    matriz_0=[]
    for i in range(len(matriz[0])):
        matriz_0.append(len(matriz)*[0])
    for linha in range(len(matriz)):
        for coluna in range(len(matriz_0)):
            matriz_0[coluna][linha]=matriz[linha][coluna]
    for j in matriz_0:        
        print(j)      
rotacionar(matriz=[[1,2,3,4],
   [4,5,6,5],
   ])            