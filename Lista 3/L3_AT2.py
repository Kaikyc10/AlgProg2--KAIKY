def maior_valor(num1, num2, num3):

    maior = num1
    
    if (num2 >= num1) and (num2 >= num3):
        maior = num2
    else:
        if (num3 > num1) and (num3 >= num2):
            maior = num3

    return maior

def main():
    n1 = int(input("Digite o 1º número inteiro: "))
    n2 = int(input("Digite o 2º número inteiro: "))
    n3 = int(input("Digite o 3º número inteiro: "))

    print(f"Maior valor: {maior_valor(n1, n2, n3)}")

main()