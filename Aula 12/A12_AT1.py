def somaRecursiva(n):

    if(n == 1):
        return 1
    print(n)
    return n + somaRecursiva(n-1)

print(somaRecursiva(3))
    
