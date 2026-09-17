#tabuada usando matriz

tabuada = []

for i in range (1,11):

    linha = []
    for j in range(1,11):
        resultado = i * j
        linha.append(resultado)
    

    tabuada.append(linha)

#exbir a matriz
print("Tabuada do 1 ao 10\n")
for i in range(len(tabuada)):
    print(f"Tabuada do {i+1}")
    for j in range(len(tabuada[i])):
        print(f"{i+1} x {j+1} = {tabuada[i][j]}")

    print("-" * 30)