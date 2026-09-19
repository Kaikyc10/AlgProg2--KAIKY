numeros=[[0]*5 for i in range(5)]
soma = 0

for linha in range (len(numeros)):
    for coluna in range(len(numeros[0])):
        n = int(input("Digite um número:" ))
        numeros[linha][coluna] = n


print()
print("Tabela de Números")
for linha in range(0,len(numeros),1):
    for coluna in range(0,len(numeros[0]),1):
        print(numeros[linha][coluna], end=" ")
    print(" ")


for linha in range(len(numeros)):
    for coluna in range(len(numeros[0])):
        if linha == coluna:
            soma = soma + numeros[linha][coluna]

print("Soma diagonal principal: ", soma)



