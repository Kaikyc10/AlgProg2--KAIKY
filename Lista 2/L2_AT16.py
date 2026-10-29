import random

matriz = [[0] * 4 for i in range(3)]

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        matriz[i][j] = random.randint(0, 30)

vetor = [0] * 12
contador = 0

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        vetor[contador] = matriz[i][j]
        contador = contador + 1

vetor.sort()
vetor.reverse()
contador = 0

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        matriz[i][j] = vetor[contador]
        contador = contador + 1

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        print(matriz[i][j], end=" ")
    print()
