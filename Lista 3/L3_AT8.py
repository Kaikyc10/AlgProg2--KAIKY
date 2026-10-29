import random

def criaVetor(min, max, n):
    vetor = [0] * n

    for i in range(len(vetor)):
        vetor[i] = random.randint(min, max)

    return vetor

def main():
    min = int(input("Defina o limite inferior de um intervalo do vetor: "))
    max = int(input("Defina o limite superior de um intervalo do vetor: "))
    n = int(input("Defina a quantidade de elementos do vetor: "))

    print(criaVetor(min, max, n))

main()
