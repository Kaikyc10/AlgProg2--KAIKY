matriz = [[5] * 5 for i in range(5)]

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if i == j:
            matriz[i][j] = 1
        else:
            if i + j == len(matriz) - 1:
                matriz[i][j] = 2

                

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        print(matriz[i][j], end=" ")
    print()