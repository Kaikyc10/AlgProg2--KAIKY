def calcular_desconto(valor,desconto=0):
    return valor - (valor*desconto/100)

print(calcular_desconto(500,10))
print(calcular_desconto(500))
print(calcular_desconto(500,35))

print(calcular_desconto(desconto=10, valor=100))