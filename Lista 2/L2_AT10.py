a0 = int(input("Digite o primeiro valor da pg: "))
razao = int(input("Digite a razão da pg: "))
n = int(input("Digite o número de elementos da pg: "))

pg = [a0] * n

for i in range(1, len(pg),1):
    pg[i] = pg[i-1] * razao

print()

print(pg)
