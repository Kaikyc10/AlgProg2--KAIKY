import random

dimensao = int(input("Digite a dimensão do seu vetor: "))
min = int(input("Digite o valor mínimo do intervalo de valores: "))
max = int(input("Digite o valor máximo do intervalo de valores: "))

numeros = [0] * dimensao
total = 0

for i in range (0,len(numeros),1):
    numeros[i] = random.randint(min,max)
    total = total + numeros[i]

print(numeros)
print(f"A somas dos valores é: {total}")
media = total/len(numeros)
print(f"A média dos valores é: {media}")
