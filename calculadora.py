def media(vetor):
    return sum(vetor)/len(vetor)

def moda(vetor):
 return 0

def mediana(vetor):

    vetor = sorted(vetor)

    meio = len(vetor)//2

    if(len(vetor) %2 !=0):

        meio = (len(vetor) +1)/2
        return vetor[meio]
    else:
        
        return (vetor[meio-1] + vetor[meio])/2








meu_vetor = [4,4,6,5]

print(mediana(meu_vetor))