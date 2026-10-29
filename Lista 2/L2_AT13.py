import random

matriz = [[0] * 5 for i in range(4)]

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        matriz[i][j] = random.randint(1, 50)

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        print(matriz[i][j], end=" ")
    print()

print()

vetor = [0] * 20
contador = 0

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        vetor[contador] = matriz[i][j]
        contador = contador + 1

print(vetor)