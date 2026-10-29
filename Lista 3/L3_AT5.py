def calcular_fatorial(n):
    fatorial = 1

    for i in range(1, n+1):
        fatorial *= i

    return fatorial

def main():
    n = int(input("Digite um número inteiro positivo ou 0: "))

    print(f"Fatorial de {n}: {calcular_fatorial(n)}")

main()