n1 = 1
n2 = 1001

if (n1 %2 != 0):
    n1 = n1+1

somatorio = n1

for i in range (n1+2,n2,2):
    somatorio = somatorio + i

print(somatorio)