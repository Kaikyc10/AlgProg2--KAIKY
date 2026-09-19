numeros=[0]*10
pares = 0

for i in range (len(numeros)):
    n = int(input("Digite um número:" ))
    numeros[i] = n

    

    if numeros[i] %2 == 0:
        pares= pares + 1

print("VALORES: ", numeros)
print()
print("Maior valor digitado - ", max(numeros))
print("Menor valor digitado - ", min(numeros))
print("Média dos valores digitados - ", sum(numeros)/len(numeros))
print("Quantidade de pares: ", pares)


    