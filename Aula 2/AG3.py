numeros = [10,20,30,40,50]
print ("Vetor completo: ")
print(numeros)
print()

#Percorrer utilizando os próprios elementos
print("percorrendo pelos valores(for each):")
for numero in numeros:
    print(numero)
print()

#percorrer utilizando os índices
print("Percorrendo pelos índices")
for indice in range(len(numeros)):
    print(f"Índice{indice} -> {numeros[indice]}")
print()

numeros[2] = 99

numeros.append(60)

numeros.pop(0)
print("Novo vetor")
print(numeros)

numeros.pop()
print("Novo vetor")
print(numeros)

print("Quantidade - len(): ", len(numeros))
print("Maior - max(): ", max(numeros))
print("Mínimo - min(): ", min(numeros))
print("Soma - sum()", sum(numeros))

print("Média = Calculo: ", sum(numeros)/len(numeros))


print("Criando uma matriz de nota")

notas = [
    [8,9,10],
    [7,8,9],
    [2,2,1]
]

print("Tabela de notas")
for linha in notas:
    for nota in linha:
        print(f"{nota:4}",end = " ")

    print()

print()
print("Acessando elementos")
print("Primeira nota:",notas[0][0])
print("Ultima nota:",notas[2][2])