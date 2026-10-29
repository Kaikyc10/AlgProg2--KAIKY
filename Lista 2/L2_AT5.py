import random

numeros = [0] * 6

for i in range(0,len(numeros),1):
    numeros[i] = random.randint(1, 60)

print(numeros)