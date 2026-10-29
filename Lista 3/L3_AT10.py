def contaParesVetor(v):
    contador = 0

    for i in range(len(v)):
        if v[i] % 2 == 0:
            contador = contador + 1

    return contador

def main():
    n = int(input("Defina a quantidade de elementos do vetor: "))
    vetor = [0] * n

    for i in range(len(vetor)):
        vetor[i] = int(input(f"Digite o {i+1}º elemento do vetor: "))

    print(f"Quantidade de números pares no vetor: {contaParesVetor(vetor)}")

main()