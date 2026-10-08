def media(*notas):
    total = sum(notas)

    return total/len(notas)




def maior_nota(*notas):
    maior = 0
    for nota in notas:
        if(notas[nota] > maior):
            maior = notas[nota]
    
    return maior


lista = [10,9,8,7,3]
media(*lista)
maior_nota(*lista)