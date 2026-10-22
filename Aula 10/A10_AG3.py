#soma dos elementos de uma lista

def somar_lista(lista):
    if(len(lista) == 0):
        return 0
    
    return lista[0] +somar_lista(lista[1:])

numeros= [2,4,6,8]

print(somar_lista(numeros))