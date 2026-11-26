def pares(n):

    if (n == 0):
        return 0

    if (n %2 != 0):
        n = n-1

    print(n)

    return pares (n-2)

#print(pares(10))

def somar_pares(n):

    

    if (n == 0):
        return 0

    if(n %2 != 0):
        n = n-1

    return n + somar_pares(n-2)


#print(somar_pares(15))

def inverter (texto):

    if(len(texto)==1):
        return texto

    return inverter(texto[1:]) + texto[0]

#print(inverter("Kaiky"))