def mediaMenoresVetor(v, x):
    soma = 0
    contador = 0
    
    for i in range(len(v)):
        if v[i] < x:
            soma = soma + v[i]
            contador = contador + 1

    media = soma / contador

    return media

def main():
    n = int(input("Defina a quantidade de elementos do vetor: "))
    vetor = [0] * n

    limite = int(input("Digite o valor de referência: "))

    for i in range(len(vetor)):
        vetor[i] = int(input(f"Digite o {i+1}º elemento do vetor: "))

    print(f"Média dos números menores que {limite} do vetor: {mediaMenoresVetor(vetor, limite)}")

main()
