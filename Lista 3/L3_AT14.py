def somaMaioresVetor(v, x):
    soma = 0
    
    for i in range(len(v)):
        if v[i] > x:
            soma = soma + v[i]

    return soma

def main():
    n = int(input("Defina a quantidade de elementos do vetor: "))
    vetor = [0] * n

    limite = int(input("Digite o valor de referência: "))

    for i in range(len(vetor)):
        vetor[i] = int(input(f"Digite o {i+1}º elemento do vetor: "))

    print(f"Soma dos números maiores que {limite} do vetor: {somaMaioresVetor(vetor, limite)}")

main()
