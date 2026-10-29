import random

matriz = [[0] * 6 for i in range(7)]

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        matriz[i][j] = random.randint(1, 25)

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        print(matriz[i][j], end=" ")
    print()

print()

vetor_matriz = [0] * 42
contador = 0

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        vetor_matriz[contador] = matriz[i][j]
        contador = contador + 1

vetor_12 = [0] * 12
contador = -1

for i in range(len(vetor_12)):
    vetor_12[i] = vetor_matriz[contador]
    contador = contador - 1

vetor_12.reverse()

print(vetor_12)

print()

vetor_15 = [0] * 15
contador = -1

for i in range(len(vetor_15)):
    vetor_15[i] = vetor_matriz[contador]
    contador = contador - 1

vetor_15.reverse()

print(vetor_15)
