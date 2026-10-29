import random

numeros = [0] *10

for i in range (0,len(numeros),1):
    numeros[i] = random.randint(27,248)

print(numeros)