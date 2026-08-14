m=[[2,3,2],
   [1,7,8],
   [1,7,8]]
n=int(input("digite um numero : "))
for linha in range(3):
    for coluna in range (3):
        if n == m[linha][coluna]:
            print(f'na linha {linha} e na coluna {coluna}')
        