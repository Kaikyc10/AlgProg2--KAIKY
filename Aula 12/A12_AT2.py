def maior(lista, indice=0, maior_numero=0):
    

    if (indice == len(lista)):
        return maior_numero
    
    if(maior_numero < lista[indice]):
        maior_numero = lista[indice]

    return maior(lista, indice+1, maior_numero)


numeros = [2,86,4,87,0]

print(maior(numeros))
    
