import random

numeros = [0] * 10

for i in range(0,len(numeros),1):
    numeros[i] = random.randint(9, 37)

numeros.sort()
numeros.reverse()

print(numeros)
