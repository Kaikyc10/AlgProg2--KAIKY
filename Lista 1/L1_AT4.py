import math

def hipotenusa(co,ca):
    hip = math.sqrt(math.pow(co,2) + math.pow(ca,2))
    print(f"sua hipotenusa é : {hip}")

co = float(input("Digite o valor do Cateto Oposto: "))
ca = float(input("Digite o valor do Cateto Adjacente: "))

hipotenusa(co,ca)
