
#for i in range(3):
#    print("+", end="")

#print()

#for i in range (5):
 #   print("+", end="")
#print()

#for i in range(8):
 #   print("=", end="")
#print()


#for i in range (5):
 #   print("=", end="")
#print()

# for i in range(3):
#     print("+",end="")
# print()

def linha():
    print("-"*10)

linha()
print("FACAMP")
linha()
print("Aulas de python")
linha()

def titulo():
    print("="*50)
    print("Sistema acadêmico")
    print("="*50)

titulo()
titulo()

def desenha_mais(quantidade):
    print("+" * quantidade)

def desenha_igual(quantidade):
    print("=" * quantidade)

# desenha_mais(3)
# desenha_mais(3)
# desenha_igual(6)
# desenha_mais(5)
# desenha_mais(3)

def desenha(simbolo, quantidade):
    print((simbolo + ",") * quantidade)

desenha("*",10)