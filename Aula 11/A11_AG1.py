def fatorial (n):
    print(f"Entrou em fatorial ({n})")

    if n ==0:
        print("Caso base encontrado!")
        print("<- fatorial(0) retorna 1")
        return 1
    
    resultado_menor = fatorial(n-1)
    resultado = n * resultado_menor
    print(f"<- fatorial ({n}) retorna {n} x {resultado_menor} = {resultado}")
    
    return resultado

numero = 2000
resultado = fatorial(numero)
print(f"\nResultado final: {numero}! = {resultado}")