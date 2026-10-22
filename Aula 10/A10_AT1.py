def pares(numero):

    if(numero <= 0):
        return

    if(numero %2 !=0):
        numero = numero -1

    print(numero)

    pares(numero-1)

pares(15)