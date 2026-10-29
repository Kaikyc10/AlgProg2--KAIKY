def contaParesMatriz(m):
    contador = 0

    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] % 2 == 0:
                contador = contador + 1

    return contador

def main():
    lin = int(input("Defina a quantidade de linhas da matriz: "))
    col = int(input("Defina a quantidade de colunas da matriz: "))
    matriz = [[0] * col for i in range(lin)]

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz[i][j] = int(input(f"Digite o elemento da posição [{i}][{j}] da matriz: "))

    print(f"Quantidade de números pares na matriz: {contaParesMatriz(matriz)}")

main()
