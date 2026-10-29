import random

vetor = [0] * 10

for i in range(0,len(vetor),1):
    vetor[i] = random.randint(9, 37)

vetor.sort()

print(vetor)