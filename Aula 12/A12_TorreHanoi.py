movimentos= 0

def hanoi(n, origem, destino, auxiliar):
    global movimentos

    #caso base
    if(n==1):
        movimentos += 1
        print(f"{movimentos}: Disco 1 de {origem} para {destino}")
        return
    
    print(f"{movimentos}: Disco {n} de {origem} para {destino}")
    hanoi(n-1,origem,auxiliar,destino)

    movimentos += 1
    #print(f"{movimentos}: Disco {n} de {origem} para {destino}")

    hanoi(n-1,auxiliar, destino, origem)

quantidade = 3
hanoi(quantidade, "A","C","B")
print(f"\nTotal: {movimentos} movimentos")