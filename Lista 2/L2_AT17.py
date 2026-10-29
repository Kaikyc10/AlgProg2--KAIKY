import random

vetor = [0] * 100

for i in range(len(vetor)):
    vetor[i] = random.randint(0, 29)

vetor.sort()

print(vetor)

print()

matriz = [[-1] * 2 for i in range(30)]

for i in range(len(matriz)):
    matriz[i][0] = matriz[i-1][0] + 1

contador = 0

for i in range(len(matriz)):
    matriz[i][1] = vetor.count(contador)
    contador = contador + 1

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        print(matriz[i][j], end=" ")
    print()
