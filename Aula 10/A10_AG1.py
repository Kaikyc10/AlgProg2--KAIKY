def contagem_regressiva(numero):
   
    #caso base
    if (numero <= 0):
        print("Fogor!!!!!!")
        return
    
    print(numero)
    contagem_regressiva(numero-1)



contagem_regressiva(100)