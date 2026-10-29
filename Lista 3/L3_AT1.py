def calcular_media(num1, num2, num3, num4):
    return (num1 + num2 + num3 + num4) / 4

def main():
    n1 = int(input("Digite o 1º número inteiro: "))
    n2 = int(input("Digite o 2º número inteiro: "))
    n3 = int(input("Digite o 3º número inteiro: "))
    n4 = int(input("Digite o 4º número inteiro: "))

    print(f"Média: {calcular_media(n1, n2, n3, n4)}")

main()