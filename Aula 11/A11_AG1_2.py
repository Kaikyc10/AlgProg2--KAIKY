chamadas =0 
def fibonacci(n, chamada):
    global chamadas
    chamadas += 1

    print(f"Fibonacci {n} - chamada {chamada}")

    if (n==0):
        return 0
    
    if(n==1):
        return 1
    
    chamada1 = fibonacci(n-1,1)
    print(f"Retorno da chamada 1: {chamada1}")

    print(f"Começando a chamar a 2: {n-2}")
    chamada2 = fibonacci(n-2,2)
    
    return chamada1 + chamada2


numero = 10
resultado = fibonacci(numero,0)
print("Resultado: ", resultado)
print("Chamadas: ", chamadas)