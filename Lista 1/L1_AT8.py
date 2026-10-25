import math

def area_trapezio(base_maior,base_menor,h):
    area = ((base_maior + base_menor)/2)*h
    print(f"A área do trapézio é : {area}")

b_maior = float(input("Digite o valor da base maior: "))
b_menor = float(input("Digite o valor da base menor: "))
h = float(input("Digite o valor da altura: "))

area_trapezio(b_maior,b_menor,h)