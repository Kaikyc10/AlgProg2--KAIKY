def somar_pares(numero):

    if(numero < 0):
        return 0
    
    if(numero%2 != 0):
        numero = numero -1
    
    print(numero)
    return numero + somar_pares(numero-2)

print(somar_pares(15))