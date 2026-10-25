import math

def volume_esfera(raio):
    area = (4* (3.14159265 * math.pow(raio,3)))/3
    print(f"O volume da esfera é : {area}")

r = float(input("Digite o valor do raio: "))

volume_esfera(r)