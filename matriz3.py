m=[[1,9,8],
   [2,4,5]]
mt=[[0,0],
    [0,0],
    [0,0]]
for linha in range(2):
    for coluna in range(3):
        mt[coluna][linha]=m[linha][coluna]
for i in mt:
    print(i)        