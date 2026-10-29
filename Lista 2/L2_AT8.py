import random

numeros = [0] * 20

for i in range(0,len(numeros),1):
    numeros[i] = random.randint(7, 3756)

maior = numeros[0]
menor = numeros[0]

for i in range(1, len(numeros)):
    if menor > numeros[i]:
        menor = numeros[i]
    if maior < numeros[i]:
        maior = numeros[i]

print(numeros)
print(f"Menor valor: {menor}")
print(f"Maior valor: {maior}")