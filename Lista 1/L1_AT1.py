def soma(*numeros):
    total = sum(numeros)
    print(f"Total da soma: {total}")

n1 = int(input("Digite o 1º valor: "))
n2 = int(input("Digite o 2º valor: "))
n3 = int(input("Digite o 3º valor: "))

soma(n1,n2,n3)