lista = [[5], [], ['a', 'b'], [9,8,7,6,1], ['z','d','a','b'], [9,1]]
tm=0
for i in lista:
    if len (i)> tm:
        tm=len(i)
print(tm)        