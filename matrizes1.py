m1=[
    [1,2,],
    [6,7,]
    ]
m2=[
    [9,5,],
    [1,9,]
    ] 
mr=[
    [0,0],
    [0,0]
    ]
for linha in range(len(mr)):
    for coluna in range(len(mr)):
        mr[linha][coluna]=m1[linha][coluna]+m2[linha][coluna]
for i in mr:        
    print(i)