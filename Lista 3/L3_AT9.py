import random

def criaMatriz(min, max, lin, col):
    matriz = [[0] * col for i in range(lin)]

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz[i][j] = random.randint(min, max)

    return matriz

def main():
    min = int(input("Defina o limite inferior de um intervalo da matriz: "))
    max = int(input("Defina o limite superior de um intervalo da matriz: "))
    lin = int(input("Defina a quantidade de linhas da matriz: "))
    col = int(input("Defina a quantidade de colunas da matriz: "))

    matriz = criaMatriz(min, max, lin, col)

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j], end=" ")
        print()

main()
