import math

def area_circunferencia(raio):
    area = 3.14159265 * math.pow(raio,2)
    print(f"A área da circunferência é : {area}")

r = float(input("Digite o valor do raio: "))

area_circunferencia(r)