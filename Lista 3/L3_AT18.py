def comparaMatrizes(m1, m2):
    if (len(m1) != len(m2)) or (len(m1[0]) != len(m2[0])):
        return False
    
    contador = 0

    for i in range(len(m1)):
        for j in range(len(m1[0])):
            if m1[i][j] == m2[i][j]:
                contador = contador + 1

    if contador == len(m1) * len(m1[0]):
        return True
    else:
        return False

def main():
    lin = int(input("Defina a quantidade de linhas da primeira matriz: "))
    col = int(input("Defina a quantidade de colunas da primeira matriz: "))
    matriz1 = [[0] * col for i in range(lin)]

    print()

    for i in range(len(matriz1)):
        for j in range(len(matriz1[0])):
            matriz1[i][j] = int(input(f"Digite o elemento da posição [{i}][{j}] da primeira matriz: "))

    print()

    lin = int(input("Defina a quantidade de linhas da segunda matriz: "))
    col = int(input("Defina a quantidade de colunas da segunda matriz: "))
    matriz2 = [[0] * col for i in range(lin)]

    print()

    for i in range(len(matriz2)):
        for j in range(len(matriz2[0])):
            matriz2[i][j] = int(input(f"Digite o elemento da posição [{i}][{j}] da segunda matriz: "))

    print()

    print(f"Matrizes iguais: {comparaMatrizes(matriz1, matriz2)}")
    

main()