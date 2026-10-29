
def verificar_par(numero):
    return numero % 2 == 0

def main():
    numero = int(input("Digite um número inteiro: "))

    print(f"Número par: {verificar_par(numero)}")

main()