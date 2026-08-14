m=[[2,3,2],
   [1,7,8],
   [1,7,8]]
n=0
for i in range(3):
    for j in range(3):
        n+=m[i][j]
print(n/9)        