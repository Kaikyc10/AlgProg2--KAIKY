import random

numeros = [0] * 6

for i in range(len(numeros)):
    numeros[i] = random.randint(1, 60)



print(numeros)

for j in range(0,len(numeros),1):
    for k in range(1,len(numeros),1):
        if numeros[j]==numeros[k]:
            numeros[k] = random.randint(1,60)

print(numeros)