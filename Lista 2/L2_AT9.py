a0 = int(input("Digite o primeiro valor da PA: "))
razao = int(input("Digite a razão da PA: "))
n = int(input("Digite o número de elementos da PA: "))

pa = [a0] * n

for i in range(1, len(pa,1)):
    pa[i] = pa[i-1] + razao

print()
print(pa)