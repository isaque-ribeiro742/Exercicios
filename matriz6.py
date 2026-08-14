m=[[1,2,3],
   [4,5,6],
   [7,8,9,]]
mm=[[0,0,0],
    [0,0,0],
    [0,0,0,]]
for linha in range(3):
    for coluna in range(3):
        mm[coluna][linha]=m[2-linha][coluna]
for i in mm:
    print(i)
