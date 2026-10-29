def contaMaioresVetor(v, x):
    contador = 0
    
    for i in range(len(v)):
        if v[i] > x:
            contador = contador + 1

    return contador

def main():
    n = int(input("Defina a quantidade de elementos do vetor: "))
    vetor = [0] * n

    limite = int(input("Digite o valor de referência: "))

    for i in range(len(vetor)):
        vetor[i] = int(input(f"Digite o {i+1}º elemento do vetor: "))

    print(f"Quantidade de números maiores que {limite} no vetor: {contaMaioresVetor(vetor, limite)}")

main()