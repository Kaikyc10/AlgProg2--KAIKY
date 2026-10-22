def fatorial(n):
    #caso base
    if(n==0) or (n==1):
        return 1
    #efeito didático
    print(n)
    #recursão
    return n * fatorial(n-1)

print(fatorial(5))