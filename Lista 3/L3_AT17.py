def mediaMenoresMatriz(m, x):
    soma = 0
    contador = 0

    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] < x:
                soma = soma + m[i][j]
                contador = contador+ 1

    media = soma / contador

    return media

def main():
    lin = int(input("Defina a quantidade de linhas da matriz: "))
    col = int(input("Defina a quantidade de colunas da matriz: "))
    matriz = [[0] * col for i in range(lin)]

    limite = int(input("Digite o valor de referência: "))

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz[i][j] = int(input(f"Digite o elemento da posição [{i}][{j}] da matriz: "))

    print(f"Média dos números menores que {limite} da matriz: {mediaMenoresMatriz(matriz, limite)}")

main()