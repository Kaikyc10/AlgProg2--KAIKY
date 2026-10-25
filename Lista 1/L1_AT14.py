import random

valor = 0
for i in range(0,10,1):
    aleatorio = random.randint(7,549)
    print(aleatorio)
    valor = valor + aleatorio

media = valor/10

print(f"A média dos valores aleatórios é: {media}")