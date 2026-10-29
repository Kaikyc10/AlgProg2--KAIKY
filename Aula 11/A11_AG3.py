def mdc(a,b):
    if(b==0):
        return a
    
    return mdc (b, a%b)

n1 = int(input("Digite o 1º número: "))
n2 = int(input("Digite o 2º número: "))
resultado = mdc(n1,n2)

print(f"\nMDC({n1,n2}) = {resultado}")