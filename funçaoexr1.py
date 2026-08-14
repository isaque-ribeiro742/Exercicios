def soma_pares(n=[]):
    p=[]
    for i in n:
        if i %2 == 0:
            p.append(i)
    return sum(p)
n=[0,3,4,2,6]
print(soma_pares(n))    