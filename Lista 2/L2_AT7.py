import random

numeros = [0] * 30

for i in range(0,len(numeros),1):
    numeros[i] = random.randint(0, 9)


# EXERCÍCIO A

menores = 0
maiores_ou_iguais = 0

for i in range(0,len(numeros),1):
    if numeros[i] < 5:
        menores = menores + 1
    else:
        maiores_ou_iguais = maiores_ou_iguais + 1

print(numeros)
print(f"Qtde de valores menores que 5: {menores}")
print(f"Qtde de valores maiores ou iguais a 5: {maiores_ou_iguais}")




# EXERCÍCIO B

numero = int(input("Digite um número inteiro entre 0 e 9: "))
menores = 0
maiores_ou_iguais = 0

for i in range(0,len(numeros),1):
    if numeros[i] < numero:
        menores = menores + 1
    else:
        maiores_ou_iguais = maiores_ou_iguais + 1

print(f"Qtde de valores menores que {numero}: {menores}")
print(f"Qtde de valores maiores ou iguais a {numero}: {maiores_ou_iguais}")