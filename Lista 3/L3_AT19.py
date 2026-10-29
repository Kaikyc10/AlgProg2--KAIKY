def transposta(m):
    n = [[0] * len(m) for i in range(len(m[0]))]

    for i in range(len(n)):
        for j in range(len(n[0])):
            n[i][j] = m[j][i]

    return n

def main():
    lin = int(input("Defina a quantidade de linhas da matriz: "))
    col = int(input("Defina a quantidade de colunas da matriz: "))
    matriz = [[0] * col for i in range(lin)]

    print()

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz[i][j] = int(input(f"Digite o elemento da posição [{i}][{j}] da matriz: "))

    print()

    print("Matriz original:")

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j], end=" ")
        print()

    print()

    matriz = transposta(matriz)

    print("Matriz transposta:")

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j], end=" ")
        print()

main()
