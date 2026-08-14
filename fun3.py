def fibonacci_recursivo (n):
    if n ==1:
        return 1
    elif n==0:
        return 0
    else:
        return fibonacci_recursivo(n-2)+ fibonacci_recursivo(n-1)
print(fibonacci_recursivo(6))     