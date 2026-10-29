import random

vetor = [0] * 20

for i in range(len(vetor)):
    vetor[i] = random.randint(31, 80)

print(vetor)

print()

matriz = [[0] * 5 for i in range(4)]
contador = 0

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        matriz[i][j] = vetor[contador]
        contador = contador + 1

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        print(matriz[i][j], end=" ")
    print()
