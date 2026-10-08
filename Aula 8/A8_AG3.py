def exibir(*valores):
    print(valores)


def soma(*v):
    total = sum(v)
    print(f"Total: {total}")    

exibir(1)
exibir(1,2)

lista = [1,2,3]
exibir(lista)
exibir(*lista)

soma(*lista)
soma(1,2,3,4,5,6,7,8,9)

