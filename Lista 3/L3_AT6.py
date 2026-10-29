import math

def calcular_volume_esfera(raio):
    return 4 * math.pi * raio ** 3 / 3

def main():
    raio = float(input("Digite o comprimento do raio da esfera: "))

    print(f"Volume da esfera: {calcular_volume_esfera(raio)}")

main()