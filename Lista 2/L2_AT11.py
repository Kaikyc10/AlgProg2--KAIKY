matriz = [[5] * 5 for i in range(5)]

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if i == j:
            matriz[i][j] = 1

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        print(matriz[i][j], end=" ")
    print()


