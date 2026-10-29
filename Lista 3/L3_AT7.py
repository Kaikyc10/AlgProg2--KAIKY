import math

def calcular_raizes(a, b, c):
    d = b ** 2 - 4 * a * c

    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)

        print(f"x1 = {x1}")
        print(f"x2 = {x2}")
    
    else:
        if d == 0:
            x = -b / (2 * a)

            print(f"x1 = x2 = {x}")

        else:
            print("Equação não possui raízes reais.")

def main():
    a = float(input("Digite o valor de a da função quadrática: "))
    b = float(input("Digite o valor de b da função quadrática: "))
    c = float(input("Digite o valor de c da função quadrática: "))

    calcular_raizes(a, b, c)

main()
