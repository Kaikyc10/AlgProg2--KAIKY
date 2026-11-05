def buscaRecursiva(lista,procurado, indice=0):

    #caso base 1:
    if(indice == len(lista)):
        return -1
    
    #caso base 2:
    if(lista[indice] == procurado):
        return indice
    
    #Passo recursivo
    return buscaRecursiva(lista, procurado, indice+1)


numeros = [18,7,25,4,31,12]
posicao = buscaRecursiva(numeros,31)

if(posicao == -1):
    print("numero não encontrado")
else:
    print(f"Número encontrado no índice {posicao}")