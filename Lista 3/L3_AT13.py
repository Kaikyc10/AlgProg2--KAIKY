def contaMaioresMatriz(m, x):
    contador = 0

    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] > x:
                contador = contador + 1

    return contador

def main():
    lin = int(input("Defina a quantidade de linhas da matriz: "))
    col = int(input("Defina a quantidade de colunas da matriz: "))
    matriz = [[0] * col for i in range(lin)]

    limite = int(input("Digite o valor de referência: "))

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz[i][j] = int(input(f"Digite o elemento da posição [{i}][{j}] da matriz: "))

    print(f"Quantidade de números maiores que {limite} na matriz: {contaMaioresMatriz(matriz, limite)}")

main()